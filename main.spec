# -*- mode: python ; coding: utf-8 -*-


a = Analysis(
    ['src\\main.py'],  # Главный файл вашего проекта
    pathex=['.'],  # Путь к папкам, где находятся ваши исходные файлы
    binaries=[],  # Указываем бинарные файлы, если необходимо
    datas=[('src/workspace/*', 'workspace')],  # Добавляем собранные файлы данных
    hiddenimports=[],  # Автоматически находим все подмодули
    hookspath=[],  # Пути к хукам, если они есть
    hooksconfig={},  # Конфигурация хуков
    runtime_hooks=[],  # Хуки, выполняемые во время исполнения
    excludes=[],  # Исключаем ненужные модули
    noarchive=False,  # Не использовать архив для сборки
    optimize=0,  # Уровень оптимизации
)

# Создаем архив из всех модулей
pyz = PYZ(a.pure)

# Определяем исполняемый файл
exe = EXE(
    pyz,  # Архив pyz
    a.scripts,  # Скрипты для исполнения
    a.binaries,  # Бинарные файлы
    a.datas,  # Данные
    [],
    name='pgs',  # Имя исполняемого файла
    debug=False,  # Режим отладки
    bootloader_ignore_signals=False,  # Игнорировать сигналы загрузчика
    strip=False,  # Удалить символы отладки
    upx=True,  # Использовать UPX для сжатия
    upx_exclude=[],  # Исключить файлы из UPX
    runtime_tmpdir=None,  # Временная директория для исполнения
    console=True,  # Показывать консоль
    disable_windowed_traceback=False,  # Отключить трассировку ошибок в окне
    argv_emulation=False,  # Эмуляция аргументов командной строки (для macOS)
    target_arch=None,  # Архитектура целевой платформы
    codesign_identity=None,  # Подпись кода (для macOS)
    entitlements_file=None,  # Файл прав (для macOS)
)

# Определяем путь к директории для сборки
distpath = 'C:\\Git\\pgs\\dist'
