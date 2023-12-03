# Представления

## get books
```
class GetBooks(ListAPIView):
    permission_classes = (IsAuthenticated,)
    filter_backends = (filters.SearchFilter,)
    search_fields = ['title', 'author']
    pagination_class = LimitOffsetPagination
    queryset = Book.objects.all()
    serializer_class = BookDepthSerializer
```
## get own books
```
class GetOwnBooks(ListAPIView):
    permission_classes = (IsAuthenticated,)
    filter_backends = [filters.SearchFilter, IsOwnerFilterBackend]
    search_fields = ['title', 'author']
    pagination_class = LimitOffsetPagination
    queryset = Book.objects.all()
    serializer_class = BookDepthSerializer
```
## get book
```
class GetBook(RetrieveAPIView):
    permission_classes = (IsAuthenticated,)
    queryset = Book
    serializer_class = BookDepthSerializer

    def get_queryset(self):
        return Book.objects.filter(id=self.kwargs['pk'])
```
## create book
```
class CreateBook(CreateAPIView):
    permission_classes = (IsAuthenticated,) 
    serializer_class = BookSerializer
    
    def create(self, request, *args, **kwargs):        
        data = {
            'title': request.data.get('title'), 
            'author': request.data.get('author'), 
            'description': request.data.get('description'),
            'owner': request.user.id
        }
        serializer = self.get_serializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
```
## update book
```
class UpdateBook(UpdateAPIView):
    permission_classes = (IsAuthenticated,) 
    queryset = Book
    serializer_class = BookSerializer
    lookup_field = 'pk'

    def update(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=True)
        if instance.owner!=request.user:
            return Response({'message': 'You are not owner'}, status=status.HTTP_400_BAD_REQUEST)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
```
## delete book
```      
class DeleteBook(DestroyAPIView):
    queryset = Book
    permission_classes = (IsAuthenticated, )

    def destroy(self, request, *args, **kwargs):
        book = self.get_object()
        if book.owner == request.user:
            self.perform_destroy(book)
            return Response({'message': 'Your book successfully deleted'}, status=status.HTTP_200_OK)
        return Response({'message': 'You are not owner'}, status=status.HTTP_400_BAD_REQUEST)
```
## get exchange requests from user
```
class GetExchangeRequestsFrom(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request):
        requests = ExchangeRequest.objects.filter(book_offered__owner=request.user).order_by('to_date')
        serializer = ExchangeRequestDepthSerializer(requests, many=True)
        return Response(serializer.data) 
```   
## get exchange to user
```
class GetExchangeRequestsTo(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request):
        requests = ExchangeRequest.objects.filter(to_user=request.user).order_by('to_date')
        serializer = ExchangeRequestDepthSerializer(requests, many=True)
        return Response(serializer.data) 
```
## get exchange request
```
class GetExchangeRequest(RetrieveAPIView):
    permission_classes = (IsAuthenticated,)
    queryset = ExchangeRequest
    serializer_class = ExchangeRequestDepthSerializer

    def get_queryset(self):
        return ExchangeRequest.objects.filter(id=self.kwargs['pk'])
```    
## create exchange request
```
class CreateExchangeRequest(CreateAPIView):
    permission_classes = (IsAuthenticated,) 
    serializer_class = ExchangeRequestSerializer
    
    def create(self, request, *args, **kwargs):        
        data = {
            'from_date': request.data.get('from_date'), 
            'to_date': request.data.get('to_date'), 
            'book_offered': request.data.get('book_offered'), 
            'to_user': request.user.id
        }
        serializer = self.get_serializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
```
## update exchange request's status
```
class UpdateExchangeRequest(UpdateAPIView):
    permission_classes = (IsAuthenticated,) 
    queryset = ExchangeRequest.objects.all()
    serializer_class = ExchangeRequestStatusSerializer
    lookup_field = 'pk'

    def update(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=True)
        if instance.book_offered.owner != request.user:
            return Response({'message': 'You are not owner'}, status=status.HTTP_400_BAD_REQUEST)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
```
## get available dates for a book to make a request
```
class GetBookDates(APIView):
    permission_classes = (IsAuthenticated, )
    
    @swagger_auto_schema(
        manual_parameters=[
            openapi.Parameter('date_from', openapi.IN_QUERY, type=openapi.TYPE_STRING),
            openapi.Parameter('date_to', openapi.IN_QUERY, type=openapi.TYPE_STRING)
        ],
    )    
    def get(self, request, *args, **kwarg):
        requests = ExchangeRequest.objects.filter(book_offered=self.kwargs['pk']).exclude(status='rejected')
        start = datetime.datetime.strptime(request.query_params.get('date_from'), '%Y-%m-%d')
        end = datetime.datetime.strptime(request.query_params.get('date_to'), '%Y-%m-%d')
        date_of_range = [start + datetime.timedelta(days=delta) for delta in range((end - start).days + 1)]
        res=[]
        for res_date in date_of_range:
            if len(requests.filter(from_date__lte=res_date, to_date__gte=res_date)) == 0:
                res.append(res_date.strftime('%Y/%m/%d'))
        return Response(res)
```