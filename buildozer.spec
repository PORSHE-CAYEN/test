[app]

# Название приложения
title = Счетчик нажатий
package.name = counterapp
package.domain = org.kivy

# Версия
version = 1.0

# Иконка (опционально)
# icon.filename = icon.png

# Расположение исходного кода
source.dir = .
source.include_exts = py,png,jpg,kv,atlas,ttf

# Требования
requirements = python3, kivy

# Ориентация экрана
orientation = portrait

# Полноэкранный режим
fullscreen = 0

# Размер окна (для отладки на ПК)
window.width = 400
window.height = 600

# Android специфичные настройки

# Минимальная версия Android SDK
android.minapi = 21

# Целевая версия Android SDK
android.api = 30

# Разрешения для Android
# android.permissions = INTERNET, WRITE_EXTERNAL_STORAGE, READ_EXTERNAL_STORAGE

# Разрешения (минимум для работы приложения)
android.permissions = 

# Архитектура Android
android.arch = arm64-v8a, armeabi-v7a

# Разрешить локальное хранилище
android.private_storage = True

# Цвет фона при загрузке
# android.presplash_color = #FFFFFF

# Файл splash screen (опционально)
# presplash.filename = presplash.png

# Версия Kivy
osx.kivy_version = 2.1.0

# Размеры окна для iOS/OSX
fullscreen = 0

# Логирование
[buildozer]
log_level = 2
warn_on_root = 1

# Дополнительные настройки
[app:source]
# Можно добавить дополнительные исходные файлы
# include_exts = 

[app:android]
# Ключ для подписи (для release сборки)
# android.release_keystore = 
# android.release_keystore_password = 
# android.release_keyalias = 
# android.release_keypassword = 

# Специфичные для Android настройки
android.accept_sdk_license = True

# Ускорить сборку (кеширование)
android.skip_build = False

[app:ios]
# Настройки для iOS если нужно

# Установка дополнительных библиотек (если понадобятся)
#[app:android.p4a]
#p4a.source_dir = 
#extra_args = [app]

# Название приложения
title = Счетчик нажатий
package.name = counterapp
package.domain = org.kivy

# Версия
version = 1.0

# Иконка (опционально)
# icon.filename = icon.png

# Расположение исходного кода
source.dir = .
source.include_exts = py,png,jpg,kv,atlas,ttf

# Требования
requirements = python3, kivy

# Ориентация экрана
orientation = portrait

# Полноэкранный режим
fullscreen = 0

# Размер окна (для отладки на ПК)
window.width = 400
window.height = 600

# Android специфичные настройки

# Минимальная версия Android SDK
android.minapi = 21

# Целевая версия Android SDK
android.api = 30

# Разрешения для Android
# android.permissions = INTERNET, WRITE_EXTERNAL_STORAGE, READ_EXTERNAL_STORAGE

# Разрешения (минимум для работы приложения)
android.permissions = 

# Архитектура Android
android.arch = arm64-v8a, armeabi-v7a

# Разрешить локальное хранилище
android.private_storage = True

# Цвет фона при загрузке
# android.presplash_color = #FFFFFF

# Файл splash screen (опционально)
# presplash.filename = presplash.png

# Версия Kivy
osx.kivy_version = 2.1.0

# Размеры окна для iOS/OSX
fullscreen = 0

# Логирование
[buildozer]
log_level = 2
warn_on_root = 1

# Дополнительные настройки
[app:source]
# Можно добавить дополнительные исходные файлы
# include_exts = 

[app:android]
# Ключ для подписи (для release сборки)
# android.release_keystore = 
# android.release_keystore_password = 
# android.release_keyalias = 
# android.release_keypassword = 

# Специфичные для Android настройки
android.accept_sdk_license = True

# Ускорить сборку (кеширование)
android.skip_build = False

[app:ios]
# Настройки для iOS если нужно

# Установка дополнительных библиотек (если понадобятся)
#[app:android.p4a]
#p4a.source_dir = 
#extra_args = 