for file in \
"C:/Users/apce1/Desktop/УЧЕБА/Веб-программирование/ITMO_ICT_WebDevelopment_2023-2024/students/к3343d/labs/Nikiforov_Arsen/лаб3/hotel_management/hotel_api/admin.py" \
"C:/Users/apce1/Desktop/УЧЕБА/Веб-программирование/ITMO_ICT_WebDevelopment_2023-2024/students/к3343d/labs/Nikiforov_Arsen/лаб3/hotel_management/hotel_api/urls.py" \
"C:/Users/apce1/Desktop/УЧЕБА/Веб-программирование/ITMO_ICT_WebDevelopment_2023-2024/students/к3343d/labs/Nikiforov_Arsen/лаб3/hotel_management/hotel_api/serializers.py" \
"C:/Users/apce1/Desktop/УЧЕБА/Веб-программирование/ITMO_ICT_WebDevelopment_2023-2024/students/к3343d/labs/Nikiforov_Arsen/лаб3/hotel_management/hotel_api/models.py" \
"C:/Users/apce1/Desktop/УЧЕБА/Веб-программирование/ITMO_ICT_WebDevelopment_2023-2024/students/к3343d/labs/Nikiforov_Arsen/лаб3/hotel_management/hotel_api/views.py" \
"C:/Users/apce1/Desktop/УЧЕБА/Веб-программирование/ITMO_ICT_WebDevelopment_2023-2024/students/к3343d/labs/Nikiforov_Arsen/лаб3/hotel_management/hotel_api/templates/hotel_api/rooms_list.html" \
"C:/Users/apce1/Desktop/УЧЕБА/Веб-программирование/ITMO_ICT_WebDevelopment_2023-2024/students/к3343d/labs/Nikiforov_Arsen/лаб3/hotel_management/hotel_api/templates/hotel_api/menu.html" \
"C:/Users/apce1/Desktop/УЧЕБА/Веб-программирование/ITMO_ICT_WebDevelopment_2023-2024/students/к3343d/labs/Nikiforov_Arsen/лаб3/hotel_management/hotel_management/settings.py" \
"C:/Users/apce1/Desktop/УЧЕБА/Веб-программирование/ITMO_ICT_WebDevelopment_2023-2024/students/к3343d/labs/Nikiforov_Arsen/лаб3/hotel_management/hotel_management/urls.py" \
"C:/Users/apce1/Desktop/УЧЕБА/Веб-программирование/ITMO_ICT_WebDevelopment_2023-2024/students/к3343d/labs/Nikiforov_Arsen/лаб3/hotel_management/hotel_api/templates/registration/register.html" \
"C:/Users/apce1/Desktop/УЧЕБА/Веб-программирование/ITMO_ICT_WebDevelopment_2023-2024/students/к3343d/labs/Nikiforov_Arsen/лаб3/hotel_management/hotel_api/templates/registration/login.html" \
"C:/Users/apce1/Desktop/УЧЕБА/Веб-программирование/ITMO_ICT_WebDevelopment_2023-2024/students/к3343d/labs/Nikiforov_Arsen/лаб3/hotel_management/hotel_api/forms.py" \

do 
    echo -e "\n\n\n\n\n\n\n\n\n\n\n\n\nFile: $file\n"
    cat "$file"
done > сохранено.txt
