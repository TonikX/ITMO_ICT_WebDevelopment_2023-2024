for file in warriors_app/admin.py warriors_app/apps.py warriors_app/models.py warriors_app/serializers.py warriors_app/urls.py warriors_app/views.py warriors_project/urls.py; do
    echo "Path: $file" >> СКОПИРОВАНО_ПРОГРАММЫ.txt
    cat "$file" >> СКОПИРОВАНО_ПРОГРАММЫ.txt
    printf "\n\n\n\n\n" >> СКОПИРОВАНО_ПРОГРАММЫ.txt
done
