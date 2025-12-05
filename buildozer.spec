[app]

# Название приложения (отображается на телефоне)
title = Счетчик нажатий

# Имя пакета (должно быть уникальным)
package.name = counterapp

# Домен пакета
package.domain = org.kivy.counter

# Путь к исходникам
source.dir = .

# Включаемые расширения файлов
source.include_exts = py,png,jpg,kv,atlas,ttf

# Версия приложения
version = 1.0

# Требования
requirements = python3, kivy==2.1.0

# Ориентация экрана
orientation = portrait

# Не использовать полноэкранный режим
fullscreen = 0

# Размеры окна (для отладки на ПК)
window.width = 400
window.height = 600

#
# Android настройки
#

# Минимальная версия Android
android.minapi = 21

# Целевая версия Android
android.api = 30

# Разрешения (пусто - не нужны)
android.permissions = 

# Архитектура
android.arch = arm64-v8a, armeabi-v7a

# Использовать приватное хранилище
android.private_storage = True

# Принять лицензии SDK автоматически
android.accept_sdk_license = True

# Цвет заставки при загрузке
android.presplash_color = #FFFFFF

# Иконка (если добавите файл icon.png)
# icon.filename = icon.png

# Заставка при загрузке (если добавите файл)
# presplash.filename = presplash.png

# Информация об авторе
author = Your Name

# Полное имя приложения
fullname = Счетчик нажатий

# Описание
description = Простое приложение-счетчик

#
# Настройки iOS/OSX
#

# Версия Kivy для macOS
osx.kivy_version = 2.1.0

#
# Настройки Buildozer
#
[buildozer]

# Уровень логирования (0-2)
log_level = 2

# Предупреждать при запуске от root
warn_on_root = 1

# Путь к каталогу сборки
# build_dir = ./.buildozer

# Количество параллельных сборок
# jobs = 4
