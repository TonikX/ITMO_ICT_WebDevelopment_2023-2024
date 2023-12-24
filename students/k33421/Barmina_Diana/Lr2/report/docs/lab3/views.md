# Представления
Я использовала несколько разных видов представлений, который повторялись 
по структуре, поэтому я представлю здесь несколько основных </br></br>

**Простейшее представления для вывода информации о клубах**
```

class ClubsListView(ListAPIView):
    queryset = Club.objects.all()
    serializer_class = ClubEasySerializer
        
```

**Вывод подробной информации для конкретного восхождения**
</br> Записи филтруются по id из url. Происходит проверка авторизации пользователя.
```

class ClimbingsDetailView(RetrieveAPIView):
    queryset = Climbing
    serializer_class = ClimbingsSerializer
    permission_classes = (IsAuthenticated, )

    def get_queryset(self):
        return Climbing.objects.filter(id=self.kwargs['pk'])
        
```

**Вывод списка всех восхождений**
</br> К простому выводу списка добавляется возможность фильтровать восхождения и задавать порядок записей.
```

class ClimbingsListView(ListAPIView):
    queryset = Climbing.objects.all()
    serializer_class = ClimbingEasySerializer
    filter_backends = [DjangoFilterBackend, OrderingFilter]
    ordering_fields = ['start_date_plan', 'level']
    filterset_class = ClimbingsFilter
            
```

**Создании записи участия в восхождении**
</br> Из интересного - так как данное действие выполняет только авторизованный пользователь, имеющий номер, 
здесь проводится проверка совпадения пользователя с номером в ссылке. 
Далее проводится проверка на наличие в бд записи с такими же данными, какие мы хотим создать - новая запись создается только при отсутствии идентичной записи. 
</br> </br>!!! Проверка пользователей происходит при каждом создании, изменении и удалении записи, поэтому в дальнейшем я не буду на этом акцентировать внимание.
</br>
```

class ParticipatingCreateView(generics.CreateAPIView):
    serializer_class = ParticipatingCreateSerializer
    permission_classes = (IsAuthenticated,)

    def create(self, request, *args, **kwargs):
        user_id = self.kwargs.get('user_id')
        if request.user.id == user_id:
            user = request.user
            #climbing_id = request.data.get('climbing_id')
            climbing = get_object_or_404(Climbing, id=self.kwargs.get('pk'))#climbing_id)
            participating = Participating.objects.filter(alpinist_id=user, climbing_id=climbing).first()
            if participating:
                return Response({'detail': 'Object already exists in favorites'}, status=status.HTTP_400_BAD_REQUEST)
            else:
                Participating.objects.create(alpinist_id=user, climbing_id=climbing)
            return Response({'detail': 'Favorite object created successfully'}, status=status.HTTP_201_CREATED)
        else:
            raise PermissionDenied(detail='Unauthorized/Wrong authorization')

            
```

**Изменение записи участия в восхождении**
</br> Единственное поле, которое может менять пользователь - успех восхождения
</br>
```

class ParticipatingUpdateView(generics.UpdateAPIView):
    queryset = Participating.objects.all()
    serializer_class = ParticipatingUpdateSerializer
    lookup_field = 'pk'

    def update(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=True)

        if serializer.is_valid():
            serializer.save()
            return Response({"message": "your participating updated successfully"})

        else:
            return Response({"message": "failed", "details": serializer.errors})
           
```

**Удаление записи участия в восхождении**

```

class ParticipatingDeleteView(generics.DestroyAPIView):
    queryset = Participating
    permission_classes = (IsAuthenticated, )

    def destroy(self, request, *args, **kwargs):
        user_id = self.kwargs.get('user_pk')
        part = self.get_object()
        if request.user.id == user_id and part.user.id == user_id:
            self.perform_destroy(part)
            return Response({'detail': 'Your participation successfully deleted'}, status=status.HTTP_200_OK)
        else:
            raise PermissionDenied(detail='You are unauthorized')
           
```
