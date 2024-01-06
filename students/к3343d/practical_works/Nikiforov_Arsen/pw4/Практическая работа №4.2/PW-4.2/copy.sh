# Определяем массив файлов
files=(
         
    "C:/Users/apce1/Desktop/УЧЕБА/Веб-программирование/ITMO_ICT_WebDevelopment_2023-2024/students/к3343d/practical_works/Nikiforov_Arsen/pw4/Практическая работа №4.2/PW-4.2/index.html"
    "C:/Users/apce1/Desktop/УЧЕБА/Веб-программирование/ITMO_ICT_WebDevelopment_2023-2024/students/к3343d/practical_works/Nikiforov_Arsen/pw4/Практическая работа №4.2/PW-4.2/src/App.vue"  
    "C:/Users/apce1/Desktop/УЧЕБА/Веб-программирование/ITMO_ICT_WebDevelopment_2023-2024/students/к3343d/practical_works/Nikiforov_Arsen/pw4/Практическая работа №4.2/PW-4.2/src/main.js"  		
    "C:/Users/apce1/Desktop/УЧЕБА/Веб-программирование/ITMO_ICT_WebDevelopment_2023-2024/students/к3343d/practical_works/Nikiforov_Arsen/pw4/Практическая работа №4.2/PW-4.2/src/router/index.js"  		
    "C:/Users/apce1/Desktop/УЧЕБА/Веб-программирование/ITMO_ICT_WebDevelopment_2023-2024/students/к3343d/practical_works/Nikiforov_Arsen/pw4/Практическая работа №4.2/PW-4.2/src/main.js"
    "C:/Users/apce1/Desktop/УЧЕБА/Веб-программирование/ITMO_ICT_WebDevelopment_2023-2024/students/к3343d/practical_works/Nikiforov_Arsen/pw4/Практическая работа №4.2/PW-4.2/src/server.cjs"
	"C:/Users/apce1/Desktop/УЧЕБА/Веб-программирование/ITMO_ICT_WebDevelopment_2023-2024/students/к3343d/practical_works/Nikiforov_Arsen/pw4/Практическая работа №4.2/PW-4.2/src/views/Warriors.vue"
	"C:/Users/apce1/Desktop/УЧЕБА/Веб-программирование/ITMO_ICT_WebDevelopment_2023-2024/students/к3343d/practical_works/Nikiforov_Arsen/pw4/Практическая работа №4.2/PW-4.2/src/components/WarriorForm.vue"
	"C:/Users/apce1/Desktop/УЧЕБА/Веб-программирование/ITMO_ICT_WebDevelopment_2023-2024/students/к3343d/practical_works/Nikiforov_Arsen/pw4/Практическая работа №4.2/PW-4.2/src/components/WarriorList.vue"
)


 






# Перебираем файлы и выводим их содержимое
for file in "${files[@]}"; do 
    echo -e "\n\n\n\n\n\n\n\n\n\n\n\n\nFile: $file\n" 
    cat "$file"
done > сохранено.txt
pause