for file in \
"C:/Users/apce1/Desktop/УЧЕБА/Веб-программирование/ITMO_ICT_WebDevelopment_2023-2024/students/к3343d/labs/Nikiforov_Arsen/лаб4/my-project/src/main.js" \
"C:/Users/apce1/Desktop/УЧЕБА/Веб-программирование/ITMO_ICT_WebDevelopment_2023-2024/students/к3343d/labs/Nikiforov_Arsen/лаб4/my-project/src/App.vue" \
"C:/Users/apce1/Desktop/УЧЕБА/Веб-программирование/ITMO_ICT_WebDevelopment_2023-2024/students/к3343d/labs/Nikiforov_Arsen/лаб4/my-project/src/router/index.js" \
"C:/Users/apce1/Desktop/УЧЕБА/Веб-программирование/ITMO_ICT_WebDevelopment_2023-2024/students/к3343d/labs/Nikiforov_Arsen/лаб4/my-project/src/components/RegistrationPage.vue" \
"C:/Users/apce1/Desktop/УЧЕБА/Веб-программирование/ITMO_ICT_WebDevelopment_2023-2024/students/к3343d/labs/Nikiforov_Arsen/лаб4/my-project/src/components/LoginPage.vue" \
"C:/Users/apce1/Desktop/УЧЕБА/Веб-программирование/ITMO_ICT_WebDevelopment_2023-2024/students/к3343d/labs/Nikiforov_Arsen/лаб4/my-project/src/components/UserProfile.vue" \
"C:/Users/apce1/Desktop/УЧЕБА/Веб-программирование/ITMO_ICT_WebDevelopment_2023-2024/students/к3343d/labs/Nikiforov_Arsen/лаб4/my-project/src/store.js" \
"C:/Users/apce1/Desktop/УЧЕБА/Веб-программирование/ITMO_ICT_WebDevelopment_2023-2024/students/к3343d/labs/Nikiforov_Arsen/лаб4/my-project/src/components/RoomsTable.vue" \
"C:/Users/apce1/Desktop/УЧЕБА/Веб-программирование/ITMO_ICT_WebDevelopment_2023-2024/students/к3343d/labs/Nikiforov_Arsen/лаб4/my-project/package.json" \
"C:/Users/apce1/Desktop/УЧЕБА/Веб-программирование/ITMO_ICT_WebDevelopment_2023-2024/students/к3343d/labs/Nikiforov_Arsen/лаб4/my-project/src/store.js" \
"C:/Users/apce1/Desktop/УЧЕБА/Веб-программирование/ITMO_ICT_WebDevelopment_2023-2024/students/к3343d/labs/Nikiforov_Arsen/лаб4/my-project/src/components/RoomStatistics.vue" \
"C:/Users/apce1/Desktop/УЧЕБА/Веб-программирование/ITMO_ICT_WebDevelopment_2023-2024/students/к3343d/labs/Nikiforov_Arsen/лаб4/my-project/src/components/LeaveFeedback.vue" \
"C:/Users/apce1/Desktop/УЧЕБА/Веб-программирование/ITMO_ICT_WebDevelopment_2023-2024/students/к3343d/labs/Nikiforov_Arsen/лаб4/my-project/src/components/AddReview.vue" \

do 
    echo -e "\n\n\n\n\n\n\n\n\n\n\n\n\nFile: $file\n"
    cat "$file"
done > сохранено.txt
