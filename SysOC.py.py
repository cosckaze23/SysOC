
 
import tkinter as tk
from tkinter import ttk, messagebox, scrolledtext
import threading
import platform
import subprocess
import os
import time
import json
import sys
from datetime import datetime
 
try:
    import psutil
except ImportError:
    subprocess.check_call([sys.executable, "-m", "pip", "install", "psutil", "--break-system-packages"])
    import psutil
 

LANGUAGES = {
    "tr": {
        "flag": "🇹🇷", "name": "Türkçe",
        "tab_live": "📊 Canlı İzleme",
        "tab_sys": "🖥 Sistem Bilgisi",
        "tab_oc": "🔥 Overclock",
        "tab_report": "📋 Tam Rapor",
        "tab_log": "📝 Log",
        "cpu_usage": "CPU Kullanımı",
        "cpu_freq": "CPU Frekansı",
        "cpu_temp": "CPU Sıcaklık",
        "ram_used": "RAM Kullanımı",
        "ram_pct": "RAM %",
        "disk_io": "Disk Okuma/Yazma",
        "os_section": "🖥 İşletim Sistemi",
        "cpu_section": "⚙️ CPU",
        "ram_section": "🧠 RAM",
        "net_section": "🌐 Ağ",
        "gpu_section": "🎮 GPU",
        "disk_section": "💾 Diskler",
        "os_label": "OS",
        "version_label": "Versiyon",
        "machine_label": "Makine",
        "hostname_label": "Hostname",
        "cpu_name": "Ad",
        "cpu_phys": "Fiziksel Çekirdek",
        "cpu_logic": "Mantıksal Thread",
        "cpu_maxf": "Maks Frekans",
        "cpu_minf": "Min Frekans",
        "cpu_currf": "Anlık Frekans",
        "cpu_use_pct": "CPU Kullanımı",
        "cpu_tempk": "CPU Sıcaklık",
        "ram_total": "Toplam RAM",
        "ram_used_k": "Kullanılan",
        "ram_free": "Boş",
        "ram_pct_k": "Kullanım %",
        "disk_drive": "Sürücü",
        "disk_fs": "Dosya Sistemi",
        "disk_total": "Toplam",
        "disk_used": "Kullanılan",
        "disk_pct": "Kullanım %",
        "gov_section": "⚙️ CPU Governor",
        "gov_current": "Mevcut governor",
        "gov_apply": "Governor Uygula",
        "freq_section": "📡 CPU Frekans Limiti",
        "freq_apply": "Frekans Uygula",
        "gpu_section_oc": "🎮 GPU Güç Limiti (NVIDIA)",
        "gpu_apply": "GPU Güç Uygula",
        "watt_diff": "Watt farkı",
        "profile_section": "💾 Overclock Profilleri",
        "profile_apply": "▶ Uygula",
        "profile_detail": "📋 Detay",
        "result_section": "📟 Sonuç",
        "oc_ready": "Overclock aracı hazır.",
        "platform_label": "Platform",
        "root_yes": "Evet",
        "root_no": "Hayır",
        "root_label": "Root",
        "report_refresh": "🔄 Raporu Yenile",
        "report_save": "💾 Dosyaya Kaydet",
        "log_clear": "🗑 Temizle",
        "log_save": "💾 Kaydet",
        "saved_msg": "Kaydedildi",
        "report_saved": "Rapor kaydedildi",
        "log_saved": "Log kaydedildi",
        "select_profile": "Lütfen bir profil seçin.",
        "profile_title": "Profil",
        "applying_profile": "Profil uygulanıyor",
        "report_title": "SİSTEM RAPORU",
        "net_adapters": "AĞ ADAPTÖRLERİ",
        "unknown": "Bilinmiyor",
        "no_gpu": "GPU bilgisi alınamadı (nvidia-smi veya lspci yükleyin)",
        "startup": "SysOC başlatıldı.",
        "lang_label": "Dil",
        "p_default": "Varsayılan",
        "p_balanced": "Dengeli",
        "p_perf": "Performans",
        "p_ocmax": "Overclock Max",
        "err_no_perm": "yetki yok",
        "err_invalid_freq": "Geçersiz frekans değeri",
        "err_freq_fail": "Frekans yazılamadı (sudo izni gerekebilir)",
        "err_no_nvidia": "nvidia-smi bulunamadı",
        "err_gpu": "GPU hatası",
        "err_no_support": "için destek yok",
        "gov_ok": "CPU governor",
        "plan_ok": "Güç planı",
        "freq_ok": "CPU maks frekans",
        "freq_cores": "çekirdek",
        "gpu_ok": "GPU güç limiti",
        "gpu_diff": "fark",
        "warn": "Uyarı",
        "error": "Hata",
    },
    "en": {
        "flag": "🇬🇧", "name": "English",
        "tab_live": "📊 Live Monitor",
        "tab_sys": "🖥 System Info",
        "tab_oc": "🔥 Overclock",
        "tab_report": "📋 Full Report",
        "tab_log": "📝 Log",
        "cpu_usage": "CPU Usage",
        "cpu_freq": "CPU Frequency",
        "cpu_temp": "CPU Temp",
        "ram_used": "RAM Used",
        "ram_pct": "RAM %",
        "disk_io": "Disk Read/Write",
        "os_section": "🖥 Operating System",
        "cpu_section": "⚙️ CPU",
        "ram_section": "🧠 RAM",
        "net_section": "🌐 Network",
        "gpu_section": "🎮 GPU",
        "disk_section": "💾 Disks",
        "os_label": "OS",
        "version_label": "Version",
        "machine_label": "Machine",
        "hostname_label": "Hostname",
        "cpu_name": "Name",
        "cpu_phys": "Physical Cores",
        "cpu_logic": "Logical Threads",
        "cpu_maxf": "Max Frequency",
        "cpu_minf": "Min Frequency",
        "cpu_currf": "Current Frequency",
        "cpu_use_pct": "CPU Usage",
        "cpu_tempk": "CPU Temp",
        "ram_total": "Total RAM",
        "ram_used_k": "Used",
        "ram_free": "Free",
        "ram_pct_k": "Usage %",
        "disk_drive": "Drive",
        "disk_fs": "File System",
        "disk_total": "Total",
        "disk_used": "Used",
        "disk_pct": "Usage %",
        "gov_section": "⚙️ CPU Governor",
        "gov_current": "Current governor",
        "gov_apply": "Apply Governor",
        "freq_section": "📡 CPU Frequency Limit",
        "freq_apply": "Apply Frequency",
        "gpu_section_oc": "🎮 GPU Power Limit (NVIDIA)",
        "gpu_apply": "Apply GPU Power",
        "watt_diff": "Watt offset",
        "profile_section": "💾 Overclock Profiles",
        "profile_apply": "▶ Apply",
        "profile_detail": "📋 Detail",
        "result_section": "📟 Output",
        "oc_ready": "Overclock tool ready.",
        "platform_label": "Platform",
        "root_yes": "Yes",
        "root_no": "No",
        "root_label": "Root",
        "report_refresh": "🔄 Refresh Report",
        "report_save": "💾 Save to File",
        "log_clear": "🗑 Clear",
        "log_save": "💾 Save",
        "saved_msg": "Saved",
        "report_saved": "Report saved",
        "log_saved": "Log saved",
        "select_profile": "Please select a profile.",
        "profile_title": "Profile",
        "applying_profile": "Applying profile",
        "report_title": "SYSTEM REPORT",
        "net_adapters": "NETWORK ADAPTERS",
        "unknown": "Unknown",
        "no_gpu": "GPU info unavailable (install nvidia-smi or lspci)",
        "startup": "SysOC started.",
        "lang_label": "Language",
        "p_default": "Default",
        "p_balanced": "Balanced",
        "p_perf": "Performance",
        "p_ocmax": "Overclock Max",
        "err_no_perm": "no permission",
        "err_invalid_freq": "Invalid frequency value",
        "err_freq_fail": "Cannot write frequency (sudo required)",
        "err_no_nvidia": "nvidia-smi not found",
        "err_gpu": "GPU error",
        "err_no_support": "not supported for",
        "gov_ok": "CPU governor",
        "plan_ok": "Power plan",
        "freq_ok": "CPU max frequency",
        "freq_cores": "cores",
        "gpu_ok": "GPU power limit",
        "gpu_diff": "offset",
        "warn": "Warning",
        "error": "Error",
    },
    "de": {
        "flag": "🇩🇪", "name": "Deutsch",
        "tab_live": "📊 Live-Monitor",
        "tab_sys": "🖥 Systeminfo",
        "tab_oc": "🔥 Übertakten",
        "tab_report": "📋 Vollbericht",
        "tab_log": "📝 Log",
        "cpu_usage": "CPU-Auslastung",
        "cpu_freq": "CPU-Frequenz",
        "cpu_temp": "CPU-Temperatur",
        "ram_used": "RAM Genutzt",
        "ram_pct": "RAM %",
        "disk_io": "Disk Lesen/Schreiben",
        "os_section": "🖥 Betriebssystem",
        "cpu_section": "⚙️ CPU",
        "ram_section": "🧠 RAM",
        "net_section": "🌐 Netzwerk",
        "gpu_section": "🎮 GPU",
        "disk_section": "💾 Laufwerke",
        "os_label": "OS",
        "version_label": "Version",
        "machine_label": "Maschine",
        "hostname_label": "Hostname",
        "cpu_name": "Name",
        "cpu_phys": "Physische Kerne",
        "cpu_logic": "Logische Threads",
        "cpu_maxf": "Max. Frequenz",
        "cpu_minf": "Min. Frequenz",
        "cpu_currf": "Aktuelle Frequenz",
        "cpu_use_pct": "CPU-Auslastung",
        "cpu_tempk": "CPU-Temperatur",
        "ram_total": "Gesamt RAM",
        "ram_used_k": "Genutzt",
        "ram_free": "Frei",
        "ram_pct_k": "Auslastung %",
        "disk_drive": "Laufwerk",
        "disk_fs": "Dateisystem",
        "disk_total": "Gesamt",
        "disk_used": "Genutzt",
        "disk_pct": "Auslastung %",
        "gov_section": "⚙️ CPU-Governor",
        "gov_current": "Aktueller Governor",
        "gov_apply": "Governor anwenden",
        "freq_section": "📡 CPU-Frequenzlimit",
        "freq_apply": "Frequenz anwenden",
        "gpu_section_oc": "🎮 GPU-Leistungslimit (NVIDIA)",
        "gpu_apply": "GPU-Leistung anwenden",
        "watt_diff": "Watt-Versatz",
        "profile_section": "💾 Übertaktprofile",
        "profile_apply": "▶ Anwenden",
        "profile_detail": "📋 Details",
        "result_section": "📟 Ausgabe",
        "oc_ready": "Übertakttool bereit.",
        "platform_label": "Plattform",
        "root_yes": "Ja",
        "root_no": "Nein",
        "root_label": "Root",
        "report_refresh": "🔄 Bericht aktualisieren",
        "report_save": "💾 In Datei speichern",
        "log_clear": "🗑 Löschen",
        "log_save": "💾 Speichern",
        "saved_msg": "Gespeichert",
        "report_saved": "Bericht gespeichert",
        "log_saved": "Log gespeichert",
        "select_profile": "Bitte ein Profil auswählen.",
        "profile_title": "Profil",
        "applying_profile": "Profil wird angewendet",
        "report_title": "SYSTEMBERICHT",
        "net_adapters": "NETZWERKADAPTER",
        "unknown": "Unbekannt",
        "no_gpu": "GPU-Info nicht verfügbar (nvidia-smi oder lspci installieren)",
        "startup": "SysOC gestartet.",
        "lang_label": "Sprache",
        "p_default": "Standard",
        "p_balanced": "Ausgewogen",
        "p_perf": "Leistung",
        "p_ocmax": "Übertakten Max",
        "err_no_perm": "keine Berechtigung",
        "err_invalid_freq": "Ungültiger Frequenzwert",
        "err_freq_fail": "Frequenz kann nicht geschrieben werden (sudo erforderlich)",
        "err_no_nvidia": "nvidia-smi nicht gefunden",
        "err_gpu": "GPU-Fehler",
        "err_no_support": "nicht unterstützt für",
        "gov_ok": "CPU-Governor",
        "plan_ok": "Energieplan",
        "freq_ok": "CPU Max-Frequenz",
        "freq_cores": "Kerne",
        "gpu_ok": "GPU-Leistungslimit",
        "gpu_diff": "Versatz",
        "warn": "Warnung",
        "error": "Fehler",
    },
    "fr": {
        "flag": "🇫🇷", "name": "Français",
        "tab_live": "📊 Surveillance",
        "tab_sys": "🖥 Infos système",
        "tab_oc": "🔥 Overclocking",
        "tab_report": "📋 Rapport complet",
        "tab_log": "📝 Journal",
        "cpu_usage": "Utilisation CPU",
        "cpu_freq": "Fréquence CPU",
        "cpu_temp": "Température CPU",
        "ram_used": "RAM utilisée",
        "ram_pct": "RAM %",
        "disk_io": "Lecture/Écriture disque",
        "os_section": "🖥 Système d'exploitation",
        "cpu_section": "⚙️ CPU",
        "ram_section": "🧠 RAM",
        "net_section": "🌐 Réseau",
        "gpu_section": "🎮 GPU",
        "disk_section": "💾 Disques",
        "os_label": "OS",
        "version_label": "Version",
        "machine_label": "Machine",
        "hostname_label": "Nom d'hôte",
        "cpu_name": "Nom",
        "cpu_phys": "Cœurs physiques",
        "cpu_logic": "Threads logiques",
        "cpu_maxf": "Fréquence max",
        "cpu_minf": "Fréquence min",
        "cpu_currf": "Fréquence actuelle",
        "cpu_use_pct": "Utilisation CPU",
        "cpu_tempk": "Température CPU",
        "ram_total": "RAM totale",
        "ram_used_k": "Utilisée",
        "ram_free": "Libre",
        "ram_pct_k": "Utilisation %",
        "disk_drive": "Lecteur",
        "disk_fs": "Système de fichiers",
        "disk_total": "Total",
        "disk_used": "Utilisé",
        "disk_pct": "Utilisation %",
        "gov_section": "⚙️ Gouverneur CPU",
        "gov_current": "Gouverneur actuel",
        "gov_apply": "Appliquer le gouverneur",
        "freq_section": "📡 Limite de fréquence CPU",
        "freq_apply": "Appliquer la fréquence",
        "gpu_section_oc": "🎮 Limite de puissance GPU (NVIDIA)",
        "gpu_apply": "Appliquer puissance GPU",
        "watt_diff": "Décalage en watts",
        "profile_section": "💾 Profils d'overclocking",
        "profile_apply": "▶ Appliquer",
        "profile_detail": "📋 Détails",
        "result_section": "📟 Résultat",
        "oc_ready": "Outil d'overclocking prêt.",
        "platform_label": "Plateforme",
        "root_yes": "Oui",
        "root_no": "Non",
        "root_label": "Root",
        "report_refresh": "🔄 Actualiser le rapport",
        "report_save": "💾 Enregistrer dans un fichier",
        "log_clear": "🗑 Effacer",
        "log_save": "💾 Enregistrer",
        "saved_msg": "Enregistré",
        "report_saved": "Rapport enregistré",
        "log_saved": "Journal enregistré",
        "select_profile": "Veuillez sélectionner un profil.",
        "profile_title": "Profil",
        "applying_profile": "Application du profil",
        "report_title": "RAPPORT SYSTÈME",
        "net_adapters": "ADAPTATEURS RÉSEAU",
        "unknown": "Inconnu",
        "no_gpu": "Infos GPU indisponibles (installez nvidia-smi ou lspci)",
        "startup": "SysOC démarré.",
        "lang_label": "Langue",
        "p_default": "Défaut",
        "p_balanced": "Équilibré",
        "p_perf": "Performance",
        "p_ocmax": "Overclocking Max",
        "err_no_perm": "pas de permission",
        "err_invalid_freq": "Valeur de fréquence invalide",
        "err_freq_fail": "Impossible d'écrire la fréquence (sudo requis)",
        "err_no_nvidia": "nvidia-smi introuvable",
        "err_gpu": "Erreur GPU",
        "err_no_support": "non pris en charge pour",
        "gov_ok": "Gouverneur CPU",
        "plan_ok": "Plan d'alimentation",
        "freq_ok": "Fréquence max CPU",
        "freq_cores": "cœurs",
        "gpu_ok": "Limite puissance GPU",
        "gpu_diff": "décalage",
        "warn": "Avertissement",
        "error": "Erreur",
    },
    "es": {
        "flag": "🇪🇸", "name": "Español",
        "tab_live": "📊 Monitor en vivo",
        "tab_sys": "🖥 Info del sistema",
        "tab_oc": "🔥 Overclocking",
        "tab_report": "📋 Informe completo",
        "tab_log": "📝 Registro",
        "cpu_usage": "Uso de CPU",
        "cpu_freq": "Frecuencia CPU",
        "cpu_temp": "Temperatura CPU",
        "ram_used": "RAM usada",
        "ram_pct": "RAM %",
        "disk_io": "Lectura/Escritura disco",
        "os_section": "🖥 Sistema operativo",
        "cpu_section": "⚙️ CPU",
        "ram_section": "🧠 RAM",
        "net_section": "🌐 Red",
        "gpu_section": "🎮 GPU",
        "disk_section": "💾 Discos",
        "os_label": "SO",
        "version_label": "Versión",
        "machine_label": "Máquina",
        "hostname_label": "Hostname",
        "cpu_name": "Nombre",
        "cpu_phys": "Núcleos físicos",
        "cpu_logic": "Hilos lógicos",
        "cpu_maxf": "Frecuencia máx",
        "cpu_minf": "Frecuencia mín",
        "cpu_currf": "Frecuencia actual",
        "cpu_use_pct": "Uso de CPU",
        "cpu_tempk": "Temperatura CPU",
        "ram_total": "RAM total",
        "ram_used_k": "Usada",
        "ram_free": "Libre",
        "ram_pct_k": "Uso %",
        "disk_drive": "Unidad",
        "disk_fs": "Sistema de archivos",
        "disk_total": "Total",
        "disk_used": "Usado",
        "disk_pct": "Uso %",
        "gov_section": "⚙️ Gobernador CPU",
        "gov_current": "Gobernador actual",
        "gov_apply": "Aplicar gobernador",
        "freq_section": "📡 Límite de frecuencia CPU",
        "freq_apply": "Aplicar frecuencia",
        "gpu_section_oc": "🎮 Límite de potencia GPU (NVIDIA)",
        "gpu_apply": "Aplicar potencia GPU",
        "watt_diff": "Diferencia de vatios",
        "profile_section": "💾 Perfiles de overclocking",
        "profile_apply": "▶ Aplicar",
        "profile_detail": "📋 Detalles",
        "result_section": "📟 Resultado",
        "oc_ready": "Herramienta de overclocking lista.",
        "platform_label": "Plataforma",
        "root_yes": "Sí",
        "root_no": "No",
        "root_label": "Root",
        "report_refresh": "🔄 Actualizar informe",
        "report_save": "💾 Guardar en archivo",
        "log_clear": "🗑 Limpiar",
        "log_save": "💾 Guardar",
        "saved_msg": "Guardado",
        "report_saved": "Informe guardado",
        "log_saved": "Registro guardado",
        "select_profile": "Por favor selecciona un perfil.",
        "profile_title": "Perfil",
        "applying_profile": "Aplicando perfil",
        "report_title": "INFORME DEL SISTEMA",
        "net_adapters": "ADAPTADORES DE RED",
        "unknown": "Desconocido",
        "no_gpu": "Info GPU no disponible (instala nvidia-smi o lspci)",
        "startup": "SysOC iniciado.",
        "lang_label": "Idioma",
        "p_default": "Predeterminado",
        "p_balanced": "Equilibrado",
        "p_perf": "Rendimiento",
        "p_ocmax": "Overclocking Máx",
        "err_no_perm": "sin permiso",
        "err_invalid_freq": "Valor de frecuencia inválido",
        "err_freq_fail": "No se puede escribir frecuencia (se requiere sudo)",
        "err_no_nvidia": "nvidia-smi no encontrado",
        "err_gpu": "Error GPU",
        "err_no_support": "no compatible para",
        "gov_ok": "Gobernador CPU",
        "plan_ok": "Plan de energía",
        "freq_ok": "Frecuencia máx CPU",
        "freq_cores": "núcleos",
        "gpu_ok": "Límite potencia GPU",
        "gpu_diff": "diferencia",
        "warn": "Advertencia",
        "error": "Error",
    },
    "ru": {
        "flag": "🇷🇺", "name": "Русский",
        "tab_live": "📊 Мониторинг",
        "tab_sys": "🖥 О системе",
        "tab_oc": "🔥 Разгон",
        "tab_report": "📋 Отчёт",
        "tab_log": "📝 Журнал",
        "cpu_usage": "Загрузка ЦП",
        "cpu_freq": "Частота ЦП",
        "cpu_temp": "Температура ЦП",
        "ram_used": "Занято ОЗУ",
        "ram_pct": "ОЗУ %",
        "disk_io": "Чтение/Запись диска",
        "os_section": "🖥 Операционная система",
        "cpu_section": "⚙️ ЦП",
        "ram_section": "🧠 ОЗУ",
        "net_section": "🌐 Сеть",
        "gpu_section": "🎮 ГП",
        "disk_section": "💾 Диски",
        "os_label": "ОС",
        "version_label": "Версия",
        "machine_label": "Архитектура",
        "hostname_label": "Имя хоста",
        "cpu_name": "Название",
        "cpu_phys": "Физ. ядра",
        "cpu_logic": "Логич. потоки",
        "cpu_maxf": "Макс. частота",
        "cpu_minf": "Мин. частота",
        "cpu_currf": "Текущая частота",
        "cpu_use_pct": "Загрузка ЦП",
        "cpu_tempk": "Температура ЦП",
        "ram_total": "Всего ОЗУ",
        "ram_used_k": "Занято",
        "ram_free": "Свободно",
        "ram_pct_k": "Занято %",
        "disk_drive": "Диск",
        "disk_fs": "Файловая система",
        "disk_total": "Всего",
        "disk_used": "Занято",
        "disk_pct": "Занято %",
        "gov_section": "⚙️ Регулятор ЦП",
        "gov_current": "Текущий регулятор",
        "gov_apply": "Применить регулятор",
        "freq_section": "📡 Лимит частоты ЦП",
        "freq_apply": "Применить частоту",
        "gpu_section_oc": "🎮 Лимит мощности ГП (NVIDIA)",
        "gpu_apply": "Применить мощность ГП",
        "watt_diff": "Смещение Вт",
        "profile_section": "💾 Профили разгона",
        "profile_apply": "▶ Применить",
        "profile_detail": "📋 Подробнее",
        "result_section": "📟 Вывод",
        "oc_ready": "Инструмент разгона готов.",
        "platform_label": "Платформа",
        "root_yes": "Да",
        "root_no": "Нет",
        "root_label": "Root",
        "report_refresh": "🔄 Обновить отчёт",
        "report_save": "💾 Сохранить в файл",
        "log_clear": "🗑 Очистить",
        "log_save": "💾 Сохранить",
        "saved_msg": "Сохранено",
        "report_saved": "Отчёт сохранён",
        "log_saved": "Журнал сохранён",
        "select_profile": "Пожалуйста, выберите профиль.",
        "profile_title": "Профиль",
        "applying_profile": "Применение профиля",
        "report_title": "СИСТЕМНЫЙ ОТЧЁТ",
        "net_adapters": "СЕТЕВЫЕ АДАПТЕРЫ",
        "unknown": "Неизвестно",
        "no_gpu": "Инфо о ГП недоступно (установите nvidia-smi или lspci)",
        "startup": "SysOC запущен.",
        "lang_label": "Язык",
        "p_default": "По умолчанию",
        "p_balanced": "Сбалансированный",
        "p_perf": "Производительность",
        "p_ocmax": "Разгон Макс",
        "err_no_perm": "нет прав",
        "err_invalid_freq": "Неверное значение частоты",
        "err_freq_fail": "Не удалось записать частоту (нужен sudo)",
        "err_no_nvidia": "nvidia-smi не найден",
        "err_gpu": "Ошибка ГП",
        "err_no_support": "не поддерживается для",
        "gov_ok": "Регулятор ЦП",
        "plan_ok": "План питания",
        "freq_ok": "Макс. частота ЦП",
        "freq_cores": "ядер",
        "gpu_ok": "Лимит мощности ГП",
        "gpu_diff": "смещение",
        "warn": "Предупреждение",
        "error": "Ошибка",
    },
    "zh": {
        "flag": "🇨🇳", "name": "中文",
        "tab_live": "📊 实时监控",
        "tab_sys": "🖥 系统信息",
        "tab_oc": "🔥 超频",
        "tab_report": "📋 完整报告",
        "tab_log": "📝 日志",
        "cpu_usage": "CPU 使用率",
        "cpu_freq": "CPU 频率",
        "cpu_temp": "CPU 温度",
        "ram_used": "内存使用",
        "ram_pct": "内存 %",
        "disk_io": "磁盘读写",
        "os_section": "🖥 操作系统",
        "cpu_section": "⚙️ CPU",
        "ram_section": "🧠 内存",
        "net_section": "🌐 网络",
        "gpu_section": "🎮 显卡",
        "disk_section": "💾 磁盘",
        "os_label": "系统",
        "version_label": "版本",
        "machine_label": "架构",
        "hostname_label": "主机名",
        "cpu_name": "名称",
        "cpu_phys": "物理核心",
        "cpu_logic": "逻辑线程",
        "cpu_maxf": "最大频率",
        "cpu_minf": "最小频率",
        "cpu_currf": "当前频率",
        "cpu_use_pct": "CPU 使用率",
        "cpu_tempk": "CPU 温度",
        "ram_total": "总内存",
        "ram_used_k": "已用",
        "ram_free": "可用",
        "ram_pct_k": "使用率 %",
        "disk_drive": "驱动器",
        "disk_fs": "文件系统",
        "disk_total": "总计",
        "disk_used": "已用",
        "disk_pct": "使用率 %",
        "gov_section": "⚙️ CPU 调速器",
        "gov_current": "当前调速器",
        "gov_apply": "应用调速器",
        "freq_section": "📡 CPU 频率限制",
        "freq_apply": "应用频率",
        "gpu_section_oc": "🎮 GPU 功耗限制 (NVIDIA)",
        "gpu_apply": "应用 GPU 功耗",
        "watt_diff": "功率偏移 (W)",
        "profile_section": "💾 超频配置",
        "profile_apply": "▶ 应用",
        "profile_detail": "📋 详情",
        "result_section": "📟 输出",
        "oc_ready": "超频工具就绪。",
        "platform_label": "平台",
        "root_yes": "是",
        "root_no": "否",
        "root_label": "Root",
        "report_refresh": "🔄 刷新报告",
        "report_save": "💾 保存到文件",
        "log_clear": "🗑 清除",
        "log_save": "💾 保存",
        "saved_msg": "已保存",
        "report_saved": "报告已保存",
        "log_saved": "日志已保存",
        "select_profile": "请选择一个配置文件。",
        "profile_title": "配置",
        "applying_profile": "正在应用配置",
        "report_title": "系统报告",
        "net_adapters": "网络适配器",
        "unknown": "未知",
        "no_gpu": "无法获取 GPU 信息（请安装 nvidia-smi 或 lspci）",
        "startup": "SysOC 已启动。",
        "lang_label": "语言",
        "p_default": "默认",
        "p_balanced": "均衡",
        "p_perf": "性能",
        "p_ocmax": "超频最大",
        "err_no_perm": "无权限",
        "err_invalid_freq": "无效的频率值",
        "err_freq_fail": "无法写入频率（需要 sudo）",
        "err_no_nvidia": "未找到 nvidia-smi",
        "err_gpu": "GPU 错误",
        "err_no_support": "不支持",
        "gov_ok": "CPU 调速器",
        "plan_ok": "电源计划",
        "freq_ok": "CPU 最大频率",
        "freq_cores": "核心",
        "gpu_ok": "GPU 功耗限制",
        "gpu_diff": "偏移",
        "warn": "警告",
        "error": "错误",
    },
    "ja": {
        "flag": "🇯🇵", "name": "日本語",
        "tab_live": "📊 ライブ監視",
        "tab_sys": "🖥 システム情報",
        "tab_oc": "🔥 オーバークロック",
        "tab_report": "📋 フルレポート",
        "tab_log": "📝 ログ",
        "cpu_usage": "CPU使用率",
        "cpu_freq": "CPU周波数",
        "cpu_temp": "CPU温度",
        "ram_used": "RAM使用量",
        "ram_pct": "RAM %",
        "disk_io": "ディスク読み書き",
        "os_section": "🖥 オペレーティングシステム",
        "cpu_section": "⚙️ CPU",
        "ram_section": "🧠 RAM",
        "net_section": "🌐 ネットワーク",
        "gpu_section": "🎮 GPU",
        "disk_section": "💾 ディスク",
        "os_label": "OS",
        "version_label": "バージョン",
        "machine_label": "アーキテクチャ",
        "hostname_label": "ホスト名",
        "cpu_name": "名前",
        "cpu_phys": "物理コア",
        "cpu_logic": "論理スレッド",
        "cpu_maxf": "最大周波数",
        "cpu_minf": "最小周波数",
        "cpu_currf": "現在の周波数",
        "cpu_use_pct": "CPU使用率",
        "cpu_tempk": "CPU温度",
        "ram_total": "総RAM",
        "ram_used_k": "使用中",
        "ram_free": "空き",
        "ram_pct_k": "使用率 %",
        "disk_drive": "ドライブ",
        "disk_fs": "ファイルシステム",
        "disk_total": "合計",
        "disk_used": "使用済み",
        "disk_pct": "使用率 %",
        "gov_section": "⚙️ CPUガバナー",
        "gov_current": "現在のガバナー",
        "gov_apply": "ガバナーを適用",
        "freq_section": "📡 CPU周波数制限",
        "freq_apply": "周波数を適用",
        "gpu_section_oc": "🎮 GPU電力制限 (NVIDIA)",
        "gpu_apply": "GPU電力を適用",
        "watt_diff": "電力オフセット (W)",
        "profile_section": "💾 OCプロファイル",
        "profile_apply": "▶ 適用",
        "profile_detail": "📋 詳細",
        "result_section": "📟 出力",
        "oc_ready": "OCツール準備完了。",
        "platform_label": "プラットフォーム",
        "root_yes": "はい",
        "root_no": "いいえ",
        "root_label": "Root",
        "report_refresh": "🔄 レポートを更新",
        "report_save": "💾 ファイルに保存",
        "log_clear": "🗑 クリア",
        "log_save": "💾 保存",
        "saved_msg": "保存済み",
        "report_saved": "レポートが保存されました",
        "log_saved": "ログが保存されました",
        "select_profile": "プロファイルを選択してください。",
        "profile_title": "プロファイル",
        "applying_profile": "プロファイル適用中",
        "report_title": "システムレポート",
        "net_adapters": "ネットワークアダプター",
        "unknown": "不明",
        "no_gpu": "GPU情報取得不可 (nvidia-smiまたはlspciをインストール)",
        "startup": "SysOC が起動しました。",
        "lang_label": "言語",
        "p_default": "デフォルト",
        "p_balanced": "バランス",
        "p_perf": "パフォーマンス",
        "p_ocmax": "OC最大",
        "err_no_perm": "権限なし",
        "err_invalid_freq": "無効な周波数値",
        "err_freq_fail": "周波数を書き込めません (sudoが必要)",
        "err_no_nvidia": "nvidia-smiが見つかりません",
        "err_gpu": "GPUエラー",
        "err_no_support": "非対応",
        "gov_ok": "CPUガバナー",
        "plan_ok": "電源プラン",
        "freq_ok": "CPU最大周波数",
        "freq_cores": "コア",
        "gpu_ok": "GPU電力制限",
        "gpu_diff": "オフセット",
        "warn": "警告",
        "error": "エラー",
    },
    "ar": {
        "flag": "🇸🇦", "name": "العربية",
        "tab_live": "📊 المراقبة المباشرة",
        "tab_sys": "🖥 معلومات النظام",
        "tab_oc": "🔥 الرفع",
        "tab_report": "📋 التقرير الكامل",
        "tab_log": "📝 السجل",
        "cpu_usage": "استخدام المعالج",
        "cpu_freq": "تردد المعالج",
        "cpu_temp": "حرارة المعالج",
        "ram_used": "الذاكرة المستخدمة",
        "ram_pct": "الذاكرة %",
        "disk_io": "قراءة/كتابة القرص",
        "os_section": "🖥 نظام التشغيل",
        "cpu_section": "⚙️ المعالج",
        "ram_section": "🧠 الذاكرة",
        "net_section": "🌐 الشبكة",
        "gpu_section": "🎮 بطاقة الرسوميات",
        "disk_section": "💾 الأقراص",
        "os_label": "النظام",
        "version_label": "الإصدار",
        "machine_label": "المعمارية",
        "hostname_label": "اسم المضيف",
        "cpu_name": "الاسم",
        "cpu_phys": "الأنوية الفعلية",
        "cpu_logic": "الخيوط المنطقية",
        "cpu_maxf": "أقصى تردد",
        "cpu_minf": "أدنى تردد",
        "cpu_currf": "التردد الحالي",
        "cpu_use_pct": "استخدام المعالج",
        "cpu_tempk": "حرارة المعالج",
        "ram_total": "إجمالي الذاكرة",
        "ram_used_k": "المستخدم",
        "ram_free": "المتاح",
        "ram_pct_k": "الاستخدام %",
        "disk_drive": "محرك الأقراص",
        "disk_fs": "نظام الملفات",
        "disk_total": "الإجمالي",
        "disk_used": "المستخدم",
        "disk_pct": "الاستخدام %",
        "gov_section": "⚙️ حاكم المعالج",
        "gov_current": "الحاكم الحالي",
        "gov_apply": "تطبيق الحاكم",
        "freq_section": "📡 حد تردد المعالج",
        "freq_apply": "تطبيق التردد",
        "gpu_section_oc": "🎮 حد طاقة GPU (NVIDIA)",
        "gpu_apply": "تطبيق طاقة GPU",
        "watt_diff": "إزاحة الواط",
        "profile_section": "💾 ملفات تعريف الرفع",
        "profile_apply": "▶ تطبيق",
        "profile_detail": "📋 تفاصيل",
        "result_section": "📟 النتيجة",
        "oc_ready": "أداة الرفع جاهزة.",
        "platform_label": "المنصة",
        "root_yes": "نعم",
        "root_no": "لا",
        "root_label": "Root",
        "report_refresh": "🔄 تحديث التقرير",
        "report_save": "💾 حفظ إلى ملف",
        "log_clear": "🗑 مسح",
        "log_save": "💾 حفظ",
        "saved_msg": "تم الحفظ",
        "report_saved": "تم حفظ التقرير",
        "log_saved": "تم حفظ السجل",
        "select_profile": "الرجاء اختيار ملف تعريف.",
        "profile_title": "ملف التعريف",
        "applying_profile": "تطبيق ملف التعريف",
        "report_title": "تقرير النظام",
        "net_adapters": "محولات الشبكة",
        "unknown": "غير معروف",
        "no_gpu": "معلومات GPU غير متاحة (ثبّت nvidia-smi أو lspci)",
        "startup": "تم تشغيل SysOC.",
        "lang_label": "اللغة",
        "p_default": "افتراضي",
        "p_balanced": "متوازن",
        "p_perf": "الأداء",
        "p_ocmax": "الرفع الأقصى",
        "err_no_perm": "لا توجد صلاحية",
        "err_invalid_freq": "قيمة تردد غير صالحة",
        "err_freq_fail": "لا يمكن كتابة التردد (يلزم sudo)",
        "err_no_nvidia": "لم يُعثر على nvidia-smi",
        "err_gpu": "خطأ في GPU",
        "err_no_support": "غير مدعوم لـ",
        "gov_ok": "حاكم المعالج",
        "plan_ok": "خطة الطاقة",
        "freq_ok": "أقصى تردد للمعالج",
        "freq_cores": "أنوية",
        "gpu_ok": "حد طاقة GPU",
        "gpu_diff": "إزاحة",
        "warn": "تحذير",
        "error": "خطأ",
    },
    "ko": {
        "flag": "🇰🇷", "name": "한국어",
        "tab_live": "📊 실시간 모니터",
        "tab_sys": "🖥 시스템 정보",
        "tab_oc": "🔥 오버클럭",
        "tab_report": "📋 전체 보고서",
        "tab_log": "📝 로그",
        "cpu_usage": "CPU 사용률",
        "cpu_freq": "CPU 주파수",
        "cpu_temp": "CPU 온도",
        "ram_used": "RAM 사용량",
        "ram_pct": "RAM %",
        "disk_io": "디스크 읽기/쓰기",
        "os_section": "🖥 운영체제",
        "cpu_section": "⚙️ CPU",
        "ram_section": "🧠 RAM",
        "net_section": "🌐 네트워크",
        "gpu_section": "🎮 GPU",
        "disk_section": "💾 디스크",
        "os_label": "OS",
        "version_label": "버전",
        "machine_label": "아키텍처",
        "hostname_label": "호스트명",
        "cpu_name": "이름",
        "cpu_phys": "물리 코어",
        "cpu_logic": "논리 스레드",
        "cpu_maxf": "최대 주파수",
        "cpu_minf": "최소 주파수",
        "cpu_currf": "현재 주파수",
        "cpu_use_pct": "CPU 사용률",
        "cpu_tempk": "CPU 온도",
        "ram_total": "전체 RAM",
        "ram_used_k": "사용 중",
        "ram_free": "여유",
        "ram_pct_k": "사용률 %",
        "disk_drive": "드라이브",
        "disk_fs": "파일 시스템",
        "disk_total": "전체",
        "disk_used": "사용됨",
        "disk_pct": "사용률 %",
        "gov_section": "⚙️ CPU 거버너",
        "gov_current": "현재 거버너",
        "gov_apply": "거버너 적용",
        "freq_section": "📡 CPU 주파수 제한",
        "freq_apply": "주파수 적용",
        "gpu_section_oc": "🎮 GPU 전력 제한 (NVIDIA)",
        "gpu_apply": "GPU 전력 적용",
        "watt_diff": "전력 오프셋 (W)",
        "profile_section": "💾 오버클럭 프로파일",
        "profile_apply": "▶ 적용",
        "profile_detail": "📋 상세",
        "result_section": "📟 출력",
        "oc_ready": "오버클럭 도구 준비 완료.",
        "platform_label": "플랫폼",
        "root_yes": "예",
        "root_no": "아니오",
        "root_label": "Root",
        "report_refresh": "🔄 보고서 새로고침",
        "report_save": "💾 파일로 저장",
        "log_clear": "🗑 지우기",
        "log_save": "💾 저장",
        "saved_msg": "저장됨",
        "report_saved": "보고서 저장됨",
        "log_saved": "로그 저장됨",
        "select_profile": "프로파일을 선택해 주세요.",
        "profile_title": "프로파일",
        "applying_profile": "프로파일 적용 중",
        "report_title": "시스템 보고서",
        "net_adapters": "네트워크 어댑터",
        "unknown": "알 수 없음",
        "no_gpu": "GPU 정보 없음 (nvidia-smi 또는 lspci 설치 필요)",
        "startup": "SysOC 시작됨.",
        "lang_label": "언어",
        "p_default": "기본",
        "p_balanced": "균형",
        "p_perf": "성능",
        "p_ocmax": "오버클럭 최대",
        "err_no_perm": "권한 없음",
        "err_invalid_freq": "잘못된 주파수 값",
        "err_freq_fail": "주파수 쓰기 실패 (sudo 필요)",
        "err_no_nvidia": "nvidia-smi를 찾을 수 없음",
        "err_gpu": "GPU 오류",
        "err_no_support": "지원되지 않음",
        "gov_ok": "CPU 거버너",
        "plan_ok": "전원 계획",
        "freq_ok": "CPU 최대 주파수",
        "freq_cores": "코어",
        "gpu_ok": "GPU 전력 제한",
        "gpu_diff": "오프셋",
        "warn": "경고",
        "error": "오류",
    },
    "pt": {
        "flag": "🇧🇷", "name": "Português",
        "tab_live": "📊 Monitor ao Vivo",
        "tab_sys": "🖥 Info do Sistema",
        "tab_oc": "🔥 Overclock",
        "tab_report": "📋 Relatório Completo",
        "tab_log": "📝 Registro",
        "cpu_usage": "Uso da CPU",
        "cpu_freq": "Frequência CPU",
        "cpu_temp": "Temperatura CPU",
        "ram_used": "RAM Usada",
        "ram_pct": "RAM %",
        "disk_io": "Leitura/Escrita Disco",
        "os_section": "🖥 Sistema Operacional",
        "cpu_section": "⚙️ CPU",
        "ram_section": "🧠 RAM",
        "net_section": "🌐 Rede",
        "gpu_section": "🎮 GPU",
        "disk_section": "💾 Discos",
        "os_label": "SO",
        "version_label": "Versão",
        "machine_label": "Arquitetura",
        "hostname_label": "Nome do Host",
        "cpu_name": "Nome",
        "cpu_phys": "Núcleos Físicos",
        "cpu_logic": "Threads Lógicas",
        "cpu_maxf": "Freq. Máxima",
        "cpu_minf": "Freq. Mínima",
        "cpu_currf": "Freq. Atual",
        "cpu_use_pct": "Uso da CPU",
        "cpu_tempk": "Temperatura CPU",
        "ram_total": "RAM Total",
        "ram_used_k": "Usado",
        "ram_free": "Livre",
        "ram_pct_k": "Uso %",
        "disk_drive": "Drive",
        "disk_fs": "Sistema de Arquivos",
        "disk_total": "Total",
        "disk_used": "Usado",
        "disk_pct": "Uso %",
        "gov_section": "⚙️ Governador CPU",
        "gov_current": "Governador atual",
        "gov_apply": "Aplicar Governador",
        "freq_section": "📡 Limite de Frequência CPU",
        "freq_apply": "Aplicar Frequência",
        "gpu_section_oc": "🎮 Limite de Potência GPU (NVIDIA)",
        "gpu_apply": "Aplicar Potência GPU",
        "watt_diff": "Diferença de Watts",
        "profile_section": "💾 Perfis de Overclock",
        "profile_apply": "▶ Aplicar",
        "profile_detail": "📋 Detalhes",
        "result_section": "📟 Resultado",
        "oc_ready": "Ferramenta de overclock pronta.",
        "platform_label": "Plataforma",
        "root_yes": "Sim",
        "root_no": "Não",
        "root_label": "Root",
        "report_refresh": "🔄 Atualizar Relatório",
        "report_save": "💾 Salvar em Arquivo",
        "log_clear": "🗑 Limpar",
        "log_save": "💾 Salvar",
        "saved_msg": "Salvo",
        "report_saved": "Relatório salvo",
        "log_saved": "Registro salvo",
        "select_profile": "Por favor selecione um perfil.",
        "profile_title": "Perfil",
        "applying_profile": "Aplicando perfil",
        "report_title": "RELATÓRIO DO SISTEMA",
        "net_adapters": "ADAPTADORES DE REDE",
        "unknown": "Desconhecido",
        "no_gpu": "Info GPU indisponível (instale nvidia-smi ou lspci)",
        "startup": "SysOC iniciado.",
        "lang_label": "Idioma",
        "p_default": "Padrão",
        "p_balanced": "Equilibrado",
        "p_perf": "Desempenho",
        "p_ocmax": "Overclock Máx",
        "err_no_perm": "sem permissão",
        "err_invalid_freq": "Valor de frequência inválido",
        "err_freq_fail": "Não foi possível escrever frequência (sudo necessário)",
        "err_no_nvidia": "nvidia-smi não encontrado",
        "err_gpu": "Erro GPU",
        "err_no_support": "não suportado para",
        "gov_ok": "Governador CPU",
        "plan_ok": "Plano de energia",
        "freq_ok": "Freq. máx CPU",
        "freq_cores": "núcleos",
        "gpu_ok": "Limite potência GPU",
        "gpu_diff": "diferença",
        "warn": "Aviso",
        "error": "Erro",
    },
}
 
C = {
    "bg":      "#0d0f14",
    "panel":   "#131720",
    "border":  "#1e2535",
    "accent":  "#00e5ff",
    "accent2": "#7c4dff",
    "green":   "#00e676",
    "yellow":  "#ffea00",
    "red":     "#ff1744",
    "orange":  "#ff6d00",
    "text":    "#cdd3e0",
    "dim":     "#4a5568",
    "white":   "#ffffff",
}
 
FONT_MONO    = ("Courier New", 10)
FONT_MONO_LG = ("Courier New", 12, "bold")
FONT_TITLE   = ("Courier New", 14, "bold")
FONT_BIG     = ("Courier New", 22, "bold")
FONT_BODY    = ("Segoe UI", 10)
 
 
class SystemInfo:
    def __init__(self):
        self.os_name   = platform.system()
        self.os_version = platform.version()
        self.machine   = platform.machine()
        self.processor = platform.processor() or self._get_cpu_name()
        self.hostname  = platform.node()
 
    def _get_cpu_name(self):
        if self.os_name == "Linux":
            try:
                with open("/proc/cpuinfo") as f:
                    for line in f:
                        if "model name" in line:
                            return line.split(":")[1].strip()
            except Exception:
                pass
        elif self.os_name == "Windows":
            try:
                out = subprocess.check_output("wmic cpu get Name", shell=True, text=True)
                lines = [l.strip() for l in out.strip().splitlines() if l.strip()]
                return lines[1] if len(lines) > 1 else "Unknown"
            except Exception:
                pass
        return platform.processor() or "Unknown"
 
    def cpu_static(self, T: dict) -> dict:
        freq = psutil.cpu_freq()
        return {
            T["cpu_name"]: self.processor,
            T["cpu_phys"]: psutil.cpu_count(logical=False),
            T["cpu_logic"]: psutil.cpu_count(logical=True),
            T["cpu_maxf"]: f"{freq.max / 1000:.2f} GHz" if freq and freq.max else "N/A",
            T["cpu_minf"]: f"{freq.min / 1000:.2f} GHz" if freq and freq.min else "N/A",
        }
 
    def cpu_live(self, T: dict) -> dict:
        freq = psutil.cpu_freq()
        temps = {}
        try:
            t = psutil.sensors_temperatures()
            if t:
                key = next(iter(t))
                temps[T["cpu_tempk"]] = f"{t[key][0].current:.1f} °C"
        except Exception:
            temps[T["cpu_tempk"]] = "N/A"
        return {
            T["cpu_currf"]: f"{freq.current / 1000:.2f} GHz" if freq else "N/A",
            T["cpu_use_pct"]: f"{psutil.cpu_percent(interval=0.1):.1f} %",
            **temps,
        }
 
    def ram_info(self, T: dict) -> dict:
        v = psutil.virtual_memory()
        return {
            T["ram_total"]: f"{v.total / 1e9:.2f} GB",
            T["ram_used_k"]: f"{v.used / 1e9:.2f} GB",
            T["ram_free"]: f"{v.available / 1e9:.2f} GB",
            T["ram_pct_k"]: f"{v.percent:.1f} %",
        }
 
    def disk_info(self, T: dict) -> list:
        disks = []
        for p in psutil.disk_partitions():
            try:
                u = psutil.disk_usage(p.mountpoint)
                disks.append({
                    T["disk_drive"]: p.mountpoint,
                    T["disk_fs"]: p.fstype,
                    T["disk_total"]: f"{u.total / 1e9:.1f} GB",
                    T["disk_used"]: f"{u.used / 1e9:.1f} GB",
                    T["disk_pct"]: f"{u.percent:.1f} %",
                })
            except Exception:
                pass
        return disks
 
    def network_info(self) -> dict:
        addrs = psutil.net_if_addrs()
        result = {}
        for iface, addr_list in addrs.items():
            for addr in addr_list:
                if addr.family.name == "AF_INET":
                    result[iface] = addr.address
        return result
 
    def gpu_info(self, T: dict) -> str:
        if self.os_name == "Windows":
            try:
                out = subprocess.check_output(
                    "wmic path win32_VideoController get Name,AdapterRAM,CurrentRefreshRate",
                    shell=True, text=True, timeout=5
                )
                return out.strip()
            except Exception:
                pass
        elif self.os_name == "Linux":
            for cmd in [["lspci", "-v"], ["glxinfo", "-B"]]:
                try:
                    out = subprocess.check_output(cmd, text=True, timeout=5, stderr=subprocess.DEVNULL)
                    lines = [l for l in out.splitlines() if any(k in l.lower() for k in ["vga", "3d", "display", "nvidia", "amd", "intel"])]
                    if lines:
                        return "\n".join(lines[:8])
                except Exception:
                    pass
        return T["no_gpu"]
 
    def full_report(self, T: dict) -> str:
        lines = [
            "=" * 60,
            f"  {T['report_title']}  {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}",
            "=" * 60,
            "",
            f"[{T['os_section']}]",
            f"  {T['os_label']:<22}: {self.os_name} {platform.release()}",
            f"  {T['version_label']:<22}: {self.os_version[:60]}",
            f"  {T['machine_label']:<22}: {self.machine}",
            f"  {T['hostname_label']:<22}: {self.hostname}",
            "",
            f"[{T['cpu_section']}]",
        ]
        for k, v in {**self.cpu_static(T), **self.cpu_live(T)}.items():
            lines.append(f"  {k:<22}: {v}")
        lines += ["", f"[{T['ram_section']}]"]
        for k, v in self.ram_info(T).items():
            lines.append(f"  {k:<22}: {v}")
        lines += ["", f"[{T['disk_section']}]"]
        for d in self.disk_info(T):
            for k, v in d.items():
                lines.append(f"  {k:<22}: {v}")
            lines.append("")
        lines += [f"[{T['net_adapters']}]"]
        for iface, ip in self.network_info().items():
            lines.append(f"  {iface:<22}: {ip}")
        lines += ["", f"[{T['gpu_section']}]", self.gpu_info(T), "", "=" * 60]
        return "\n".join(lines)
 
 
class OverclockManager:
    def __init__(self):
        self.os_name = platform.system()
        self.log: list = []
        self._profiles = self._load_profiles()
 
    def _profile_path(self):
        return os.path.join(os.path.expanduser("~"), ".sysoc_profiles.json")
 
    def _load_profiles(self) -> dict:
        try:
            with open(self._profile_path()) as f:
                return json.load(f)
        except Exception:
            return {
                "DEFAULT":   {"cpu_governor": "powersave",   "cpu_freq_max": 0,  "gpu_power": 0},
                "BALANCED":  {"cpu_governor": "schedutil",   "cpu_freq_max": 0,  "gpu_power": 0},
                "PERF":      {"cpu_governor": "performance", "cpu_freq_max": 0,  "gpu_power": 0},
                "OC_MAX":    {"cpu_governor": "performance", "cpu_freq_max": -1, "gpu_power": 20},
            }
 
    def save_profiles(self):
        with open(self._profile_path(), "w") as f:
            json.dump(self._profiles, f, indent=2, ensure_ascii=False)
 
    def profile_keys(self) -> list:
        return list(self._profiles.keys())
 
    def get_profile(self, key: str) -> dict:
        return self._profiles.get(key, {})
 
    def set_cpu_governor(self, governor: str, T: dict) -> tuple:
        if self.os_name == "Linux":
            cores = psutil.cpu_count(logical=True)
            errors = []
            for i in range(cores):
                path = f"/sys/devices/system/cpu/cpu{i}/cpufreq/scaling_governor"
                try:
                    if os.access(path, os.W_OK):
                        with open(path, "w") as f:
                            f.write(governor)
                    else:
                        r = subprocess.run(
                            ["sudo", "tee", path],
                            input=governor.encode(), capture_output=True, timeout=5
                        )
                        if r.returncode != 0:
                            errors.append(f"cpu{i}: {T['err_no_perm']}")
                except Exception as e:
                    errors.append(str(e))
            if errors:
                return False, f"{T['warn']}: {', '.join(errors[:3])}"
            return True, f"{T['gov_ok']} → {governor} ✓"
        elif self.os_name == "Windows":
            schemes = {
                "powersave":   "a1841308-3541-4fab-bc81-f71556f20b4a",
                "balanced":    "381b4222-f694-41f0-9685-ff5bb260df2e",
                "performance": "8c5e7fda-e8bf-4a96-9a85-a6e23a8c635c",
                "schedutil":   "381b4222-f694-41f0-9685-ff5bb260df2e",
            }
            guid = schemes.get(governor, schemes["balanced"])
            try:
                subprocess.run(["powercfg", "/setactive", guid], check=True, timeout=5)
                return True, f"{T['plan_ok']} → {governor} ✓"
            except Exception as e:
                return False, f"{T['error']}: {e}"
        return False, f"{self.os_name} {T['err_no_support']} governor"
 
    def set_cpu_freq(self, max_mhz: int, T: dict) -> tuple:
        if max_mhz <= 0:
            return False, T["err_invalid_freq"]
        if self.os_name == "Linux":
            cores = psutil.cpu_count(logical=True)
            ok = 0
            for i in range(cores):
                path = f"/sys/devices/system/cpu/cpu{i}/cpufreq/scaling_max_freq"
                try:
                    val = str(max_mhz * 1000)
                    if os.access(path, os.W_OK):
                        with open(path, "w") as f:
                            f.write(val)
                        ok += 1
                    else:
                        r = subprocess.run(
                            ["sudo", "tee", path],
                            input=val.encode(), capture_output=True, timeout=5
                        )
                        if r.returncode == 0:
                            ok += 1
                except Exception:
                    pass
            if ok > 0:
                return True, f"{T['freq_ok']} → {max_mhz} MHz ({ok}/{cores} {T['freq_cores']}) ✓"
            return False, T["err_freq_fail"]
        elif self.os_name == "Windows":
            try:
                cmd = f"powercfg /setacvalueindex SCHEME_CURRENT SUB_PROCESSOR PROCFREQMAX {max_mhz}"
                subprocess.run(cmd, shell=True, check=True, timeout=5)
                subprocess.run("powercfg /setactive SCHEME_CURRENT", shell=True, check=True)
                return True, f"{T['freq_ok']} → {max_mhz} MHz ✓"
            except Exception as e:
                return False, f"{T['error']}: {e}"
        return False, f"{self.os_name} {T['err_no_support']}"
 
    def set_gpu_power_limit(self, offset_watt: int, T: dict) -> tuple:
        try:
            base = subprocess.check_output(
                ["nvidia-smi", "--query-gpu=power.limit", "--format=csv,noheader,nounits"],
                text=True, timeout=5
            ).strip()
            current = float(base)
            new_limit = int(current + offset_watt)
            subprocess.run(["nvidia-smi", f"--power-limit={new_limit}"], check=True, timeout=5)
            return True, f"{T['gpu_ok']} → {new_limit}W ({T['gpu_diff']}: +{offset_watt}W) ✓"
        except FileNotFoundError:
            return False, T["err_no_nvidia"]
        except Exception as e:
            return False, f"{T['err_gpu']}: {e}"
 
    def apply_profile(self, key: str, T: dict) -> list:
        profile = self.get_profile(key)
        results = [f"▶ {T['applying_profile']}: {key}"]
        gov = profile.get("cpu_governor")
        if gov:
            ok, msg = self.set_cpu_governor(gov, T)
            results.append(("✓ " if ok else "✗ ") + msg)
        freq = profile.get("cpu_freq_max", 0)
        if freq and freq > 0:
            ok, msg = self.set_cpu_freq(freq, T)
            results.append(("✓ " if ok else "✗ ") + msg)
        elif freq == -1:
            cpu_freq = psutil.cpu_freq()
            if cpu_freq and cpu_freq.max:
                ok, msg = self.set_cpu_freq(int(cpu_freq.max), T)
                results.append(("✓ " if ok else "✗ ") + msg)
        gpu = profile.get("gpu_power", 0)
        if gpu and gpu != 0:
            ok, msg = self.set_gpu_power_limit(gpu, T)
            results.append(("✓ " if ok else "✗ ") + msg)
        ts = datetime.now().strftime("%H:%M:%S")
        self.log.append(f"[{ts}] {T['profile_title']}: {key}")
        self.log.extend(results)
        return results
 
    def current_governor(self) -> str:
        if self.os_name == "Linux":
            try:
                with open("/sys/devices/system/cpu/cpu0/cpufreq/scaling_governor") as f:
                    return f.read().strip()
            except Exception:
                pass
        elif self.os_name == "Windows":
            try:
                out = subprocess.check_output("powercfg /getactivescheme", shell=True, text=True, timeout=5)
                if "Power saver" in out or "a1841308" in out.lower():
                    return "powersave"
                if "High performance" in out or "8c5e7fda" in out.lower():
                    return "performance"
                return "balanced"
            except Exception:
                pass
        return "unknown"
 
    def available_governors(self) -> list:
        if self.os_name == "Linux":
            try:
                with open("/sys/devices/system/cpu/cpu0/cpufreq/scaling_available_governors") as f:
                    return f.read().strip().split()
            except Exception:
                pass
        return ["powersave", "schedutil", "ondemand", "conservative", "performance"]
 
 
class SysOCApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self._lang_code = "tr"
        self.T = LANGUAGES[self._lang_code]
        self.title("SysOC — System Monitor & Overclock")
        self.configure(bg=C["bg"])
        self.geometry("1050x700")
        self.minsize(900, 600)
        self.sysinfo   = SystemInfo()
        self.ocmanager = OverclockManager()
        self._running  = True
        self._build_ui()
        self._start_live_update()
 
    def _t(self, key: str) -> str:
        return self.T.get(key, key)
 
    def _switch_language(self, code: str):
        self._lang_code = code
        self.T = LANGUAGES[code]
        for widget in self.winfo_children():
            widget.destroy()
        self._build_ui()
        self._start_live_update()
 
    def _build_ui(self):
        header = tk.Frame(self, bg=C["panel"], pady=6)
        header.pack(fill="x")
 
        tk.Label(header, text="⚡ SysOC", font=FONT_TITLE, fg=C["accent"], bg=C["panel"]).pack(side="left", padx=16)
        tk.Label(header, text=f"{self.sysinfo.os_name}  |  {self.sysinfo.hostname}", font=FONT_MONO, fg=C["dim"], bg=C["panel"]).pack(side="left", padx=10)
 
        lang_frame = tk.Frame(header, bg=C["panel"])
        lang_frame.pack(side="right", padx=10)
 
        for code, data in LANGUAGES.items():
            is_active = (code == self._lang_code)
            btn = tk.Button(
                lang_frame,
                text=data["flag"],
                font=("Segoe UI Emoji", 14),
                bg=C["accent"] if is_active else C["border"],
                fg=C["bg"] if is_active else C["text"],
                relief="flat", bd=0, padx=4, pady=2,
                cursor="hand2",
                command=lambda c=code: self._switch_language(c)
            )
            btn.pack(side="left", padx=2)
 
        self._time_lbl = tk.Label(header, text="", font=FONT_MONO, fg=C["accent2"], bg=C["panel"])
        self._time_lbl.pack(side="right", padx=16)
 
        style = ttk.Style(self)
        style.theme_use("clam")
        style.configure("TNotebook",      background=C["bg"], borderwidth=0)
        style.configure("TNotebook.Tab",  background=C["panel"], foreground=C["dim"],
                        font=FONT_BODY, padding=[14, 6], borderwidth=0)
        style.map("TNotebook.Tab",
                  background=[("selected", C["bg"])],
                  foreground=[("selected", C["accent"])])
 
        nb = ttk.Notebook(self)
        nb.pack(fill="both", expand=True)
 
        tab_live   = tk.Frame(nb, bg=C["bg"])
        tab_static = tk.Frame(nb, bg=C["bg"])
        tab_oc     = tk.Frame(nb, bg=C["bg"])
        tab_report = tk.Frame(nb, bg=C["bg"])
        tab_log    = tk.Frame(nb, bg=C["bg"])
 
        nb.add(tab_live,   text=self._t("tab_live"))
        nb.add(tab_static, text=self._t("tab_sys"))
        nb.add(tab_oc,     text=self._t("tab_oc"))
        nb.add(tab_report, text=self._t("tab_report"))
        nb.add(tab_log,    text=self._t("tab_log"))
 
        self._build_live_tab(tab_live)
        self._build_static_tab(tab_static)
        self._build_oc_tab(tab_oc)
        self._build_report_tab(tab_report)
        self._build_log_tab(tab_log)
 
    def _make_card(self, parent, label: str, color: str) -> tk.Frame:
        frame = tk.Frame(parent, bg=C["panel"], bd=0, relief="flat",
                         highlightbackground=C["border"], highlightthickness=1)
        tk.Label(frame, text=label, font=FONT_BODY, fg=C["dim"], bg=C["panel"]).pack(pady=(10, 0))
        val_lbl = tk.Label(frame, text="—", font=FONT_BIG, fg=color, bg=C["panel"])
        val_lbl.pack(pady=(2, 12))
        frame._val = val_lbl
        return frame
 
    def _make_progress(self, parent, label, style_name, row):
        tk.Label(parent, text=f"{label}:", font=FONT_MONO, fg=C["text"],
                 bg=C["panel"], width=5, anchor="w").grid(row=row, column=0, padx=(0, 8), pady=4)
        bar = ttk.Progressbar(parent, style=style_name, length=400, maximum=100)
        bar.grid(row=row, column=1, sticky="ew", padx=(0, 8))
        pct_lbl = tk.Label(parent, text="0%", font=FONT_MONO, fg=C["text"], bg=C["panel"], width=7)
        pct_lbl.grid(row=row, column=2)
        parent.columnconfigure(1, weight=1)
        return bar, pct_lbl
 
    def _make_btn(self, parent, text, cmd, color=None):
        color = color or C["accent"]
        return tk.Button(
            parent, text=text, command=cmd,
            font=FONT_MONO, fg=C["bg"], bg=color,
            activebackground=C["white"], activeforeground=C["bg"],
            relief="flat", padx=14, pady=5, cursor="hand2", bd=0
        )
 
    def _build_live_tab(self, parent):
        grid = tk.Frame(parent, bg=C["bg"])
        grid.pack(fill="both", expand=True, padx=20, pady=16)
        grid.columnconfigure((0, 1, 2), weight=1, uniform="col")
 
        self._live_cards = {}
        cards = [
            ("cpu_usage", self._t("cpu_usage"), C["accent"],  0, 0),
            ("cpu_freq",  self._t("cpu_freq"),  C["accent2"], 0, 1),
            ("cpu_temp",  self._t("cpu_temp"),  C["orange"],  0, 2),
            ("ram_used",  self._t("ram_used"),  C["green"],   1, 0),
            ("ram_pct",   self._t("ram_pct"),   C["yellow"],  1, 1),
            ("disk_io",   self._t("disk_io"),   C["dim"],     1, 2),
        ]
        for key, label, color, row, col in cards:
            card = self._make_card(grid, label, color)
            card.grid(row=row, column=col, padx=8, pady=8, sticky="nsew")
            grid.rowconfigure(row, weight=1)
            self._live_cards[key] = card
 
        pb_frame = tk.Frame(parent, bg=C["panel"], padx=16, pady=10)
        pb_frame.pack(fill="x", padx=20, pady=(0, 16))
 
        style = ttk.Style()
        style.configure("Accent.Horizontal.TProgressbar", troughcolor=C["border"], background=C["accent"], thickness=16)
        style.configure("Green.Horizontal.TProgressbar",  troughcolor=C["border"], background=C["green"],  thickness=16)
 
        self._cpu_bar = self._make_progress(pb_frame, "CPU", "Accent.Horizontal.TProgressbar", 0)
        self._ram_bar = self._make_progress(pb_frame, "RAM", "Green.Horizontal.TProgressbar",  1)
 
    def _update_live(self):
        cpu_pct = psutil.cpu_percent(interval=None)
        freq    = psutil.cpu_freq()
        mem     = psutil.virtual_memory()
        try:
            disk = psutil.disk_io_counters()
            dio  = f"R {disk.read_bytes / 1e6:.0f}MB"
        except Exception:
            dio = "N/A"
        temp_str = "N/A"
        try:
            t = psutil.sensors_temperatures()
            if t:
                key = next(iter(t))
                temp_str = f"{t[key][0].current:.0f}°C"
        except Exception:
            pass
        data = {
            "cpu_usage": f"{cpu_pct:.0f}%",
            "cpu_freq":  f"{freq.current / 1000:.2f}GHz" if freq else "N/A",
            "cpu_temp":  temp_str,
            "ram_used":  f"{mem.used / 1e9:.1f}GB",
            "ram_pct":   f"{mem.percent:.0f}%",
            "disk_io":   dio,
        }
        for key, val in data.items():
            self._live_cards[key]._val.config(text=val)
        self._cpu_bar[0]["value"] = cpu_pct
        self._cpu_bar[1].config(text=f"{cpu_pct:.0f}%")
        self._ram_bar[0]["value"] = mem.percent
        self._ram_bar[1].config(text=f"{mem.percent:.0f}%")
        self._time_lbl.config(text=datetime.now().strftime("%H:%M:%S"))
 
    def _build_static_tab(self, parent):
        scroll_frame = tk.Frame(parent, bg=C["bg"])
        scroll_frame.pack(fill="both", expand=True, padx=20, pady=16)
 
        sections = [
            (self._t("os_section"), {
                self._t("os_label"):       f"{self.sysinfo.os_name} {platform.release()}",
                self._t("version_label"):  platform.version()[:70],
                self._t("machine_label"):  self.sysinfo.machine,
                self._t("hostname_label"): self.sysinfo.hostname,
            }),
            (self._t("cpu_section"),  self.sysinfo.cpu_static(self.T)),
            (self._t("ram_section"),  self.sysinfo.ram_info(self.T)),
            (self._t("net_section"),  self.sysinfo.network_info()),
        ]
 
        for title, data in sections:
            sec = tk.LabelFrame(scroll_frame, text=f"  {title}  ", font=FONT_MONO,
                                fg=C["accent"], bg=C["panel"], bd=1, relief="solid", labelanchor="nw")
            sec.pack(fill="x", pady=6)
            for k, v in data.items():
                row = tk.Frame(sec, bg=C["panel"])
                row.pack(fill="x", padx=12, pady=2)
                tk.Label(row, text=f"{k}:", font=FONT_MONO, fg=C["dim"], bg=C["panel"], width=22, anchor="w").pack(side="left")
                tk.Label(row, text=str(v),  font=FONT_MONO, fg=C["text"], bg=C["panel"], anchor="w").pack(side="left")
 
        gpu_sec = tk.LabelFrame(scroll_frame, text=f"  {self._t('gpu_section')}  ", font=FONT_MONO,
                                fg=C["accent"], bg=C["panel"], bd=1, relief="solid", labelanchor="nw")
        gpu_sec.pack(fill="x", pady=6)
        gpu_txt = scrolledtext.ScrolledText(gpu_sec, font=FONT_MONO, fg=C["green"], bg=C["bg"],
                                            height=6, bd=0, insertbackground=C["accent"])
        gpu_txt.insert("1.0", self.sysinfo.gpu_info(self.T))
        gpu_txt.config(state="disabled")
        gpu_txt.pack(fill="x", padx=12, pady=8)
 
        disk_sec = tk.LabelFrame(scroll_frame, text=f"  {self._t('disk_section')}  ", font=FONT_MONO,
                                 fg=C["accent"], bg=C["panel"], bd=1, relief="solid", labelanchor="nw")
        disk_sec.pack(fill="x", pady=6)
        cols = [self._t("disk_drive"), self._t("disk_fs"), self._t("disk_total"), self._t("disk_used"), self._t("disk_pct")]
        tree_style = ttk.Style()
        tree_style.configure("Custom.Treeview",
                             background=C["bg"], foreground=C["text"],
                             fieldbackground=C["bg"], rowheight=24, font=FONT_MONO)
        tree_style.configure("Custom.Treeview.Heading",
                             background=C["panel"], foreground=C["accent"], font=FONT_MONO)
        tree = ttk.Treeview(disk_sec, columns=cols, show="headings", style="Custom.Treeview", height=4)
        for col in cols:
            tree.heading(col, text=col)
            tree.column(col, width=130, anchor="center")
        for d in self.sysinfo.disk_info(self.T):
            tree.insert("", "end", values=[d.get(c, "") for c in cols])
        tree.pack(fill="x", padx=12, pady=8)
 
    def _build_oc_tab(self, parent):
        left  = tk.Frame(parent, bg=C["bg"])
        right = tk.Frame(parent, bg=C["bg"])
        left.pack(side="left",  fill="both", expand=True, padx=(20, 8), pady=16)
        right.pack(side="right", fill="both", expand=True, padx=(8, 20), pady=16)
 
        gov_sec = tk.LabelFrame(left, text=f"  {self._t('gov_section')}  ", font=FONT_MONO,
                                fg=C["accent"], bg=C["panel"], bd=1, relief="solid", labelanchor="nw")
        gov_sec.pack(fill="x", pady=8)
 
        cur_gov = self.ocmanager.current_governor()
        tk.Label(gov_sec, text=f"{self._t('gov_current')}: {cur_gov}",
                 font=FONT_MONO, fg=C["green"], bg=C["panel"]).pack(pady=(8, 4))
 
        gov_options = self.ocmanager.available_governors()
        self._gov_var = tk.StringVar(value=cur_gov if cur_gov in gov_options else gov_options[0])
        for g in gov_options:
            color = C["accent"] if g == "performance" else C["text"]
            tk.Radiobutton(gov_sec, text=g, variable=self._gov_var, value=g,
                           font=FONT_MONO, fg=color, bg=C["panel"],
                           selectcolor=C["border"], activebackground=C["panel"],
                           activeforeground=C["accent"]).pack(anchor="w", padx=20)
 
        self._make_btn(tk.Frame(gov_sec, bg=C["panel"]), self._t("gov_apply"), self._apply_governor).pack()
        tk.Frame(gov_sec, bg=C["panel"]).pack(pady=4)
 
        freq_sec = tk.LabelFrame(left, text=f"  {self._t('freq_section')}  ", font=FONT_MONO,
                                 fg=C["accent"], bg=C["panel"], bd=1, relief="solid", labelanchor="nw")
        freq_sec.pack(fill="x", pady=8)
 
        freq = psutil.cpu_freq()
        max_khz = int(freq.max) if freq and freq.max else 3600
        cur_khz = int(freq.current) if freq else 3000
 
        tk.Label(freq_sec, text=f"Max: {max_khz:.0f} MHz | Now: {cur_khz:.0f} MHz",
                 font=FONT_MONO, fg=C["dim"], bg=C["panel"]).pack(pady=(8, 4))
 
        self._freq_var = tk.IntVar(value=cur_khz)
        tk.Scale(freq_sec, from_=800, to=int(max_khz * 1.15), orient="horizontal",
                 variable=self._freq_var, font=FONT_MONO, fg=C["text"], bg=C["panel"],
                 troughcolor=C["border"], activebackground=C["accent"],
                 highlightthickness=0, resolution=100, label="MHz").pack(fill="x", padx=16, pady=4)
        self._make_btn(freq_sec, self._t("freq_apply"), self._apply_freq).pack(pady=8)
 
        gpu_sec = tk.LabelFrame(left, text=f"  {self._t('gpu_section_oc')}  ", font=FONT_MONO,
                                fg=C["accent"], bg=C["panel"], bd=1, relief="solid", labelanchor="nw")
        gpu_sec.pack(fill="x", pady=8)
 
        self._gpu_var = tk.IntVar(value=0)
        tk.Scale(gpu_sec, from_=-30, to=50, orient="horizontal",
                 variable=self._gpu_var, font=FONT_MONO, fg=C["text"], bg=C["panel"],
                 troughcolor=C["border"], activebackground=C["accent2"],
                 highlightthickness=0, resolution=5,
                 label=self._t("watt_diff")).pack(fill="x", padx=16, pady=4)
        self._make_btn(gpu_sec, self._t("gpu_apply"), self._apply_gpu).pack(pady=8)
 
        prof_sec = tk.LabelFrame(right, text=f"  {self._t('profile_section')}  ", font=FONT_MONO,
                                 fg=C["accent2"], bg=C["panel"], bd=1, relief="solid", labelanchor="nw")
        prof_sec.pack(fill="x", pady=8)
 
        profile_keys = self.ocmanager.profile_keys()
        profile_labels = {
            "DEFAULT":  self._t("p_default"),
            "BALANCED": self._t("p_balanced"),
            "PERF":     self._t("p_perf"),
            "OC_MAX":   self._t("p_ocmax"),
        }
 
        self._profile_list = tk.Listbox(prof_sec, font=FONT_MONO, fg=C["text"], bg=C["bg"],
                                        selectbackground=C["accent2"], selectforeground=C["white"],
                                        bd=0, highlightthickness=0, height=5)
        for key in profile_keys:
            self._profile_list.insert("end", profile_labels.get(key, key))
        self._profile_keys = profile_keys
        self._profile_list.pack(fill="x", padx=12, pady=8)
 
        btn_row = tk.Frame(prof_sec, bg=C["panel"])
        btn_row.pack(pady=(0, 10))
        self._make_btn(btn_row, self._t("profile_apply"), self._apply_profile, C["accent2"]).pack(side="left", padx=4)
        self._make_btn(btn_row, self._t("profile_detail"), self._show_profile_detail, C["dim"]).pack(side="left", padx=4)
 
        out_sec = tk.LabelFrame(right, text=f"  {self._t('result_section')}  ", font=FONT_MONO,
                                fg=C["green"], bg=C["panel"], bd=1, relief="solid", labelanchor="nw")
        out_sec.pack(fill="both", expand=True, pady=8)
 
        self._oc_output = scrolledtext.ScrolledText(out_sec, font=FONT_MONO, fg=C["green"], bg=C["bg"],
                                                    bd=0, insertbackground=C["accent"], height=12)
        self._oc_output.pack(fill="both", expand=True, padx=8, pady=8)
        self._oc_print(self._t("oc_ready"))
 
        root_val = self._t("root_yes") if (hasattr(os, "geteuid") and os.geteuid() == 0) else self._t("root_no")
        self._oc_print(f"{self._t('platform_label')}: {platform.system()} | {self._t('root_label')}: {root_val}")
 
    def _oc_print(self, msg: str):
        ts = datetime.now().strftime("%H:%M:%S")
        self._oc_output.insert("end", f"[{ts}] {msg}\n")
        self._oc_output.see("end")
 
    def _apply_governor(self):
        gov = self._gov_var.get()
        ok, msg = self.ocmanager.set_cpu_governor(gov, self.T)
        self._oc_print(("✓ " if ok else "✗ ") + msg)
 
    def _apply_freq(self):
        mhz = self._freq_var.get()
        ok, msg = self.ocmanager.set_cpu_freq(mhz, self.T)
        self._oc_print(("✓ " if ok else "✗ ") + msg)
 
    def _apply_gpu(self):
        watt = self._gpu_var.get()
        ok, msg = self.ocmanager.set_gpu_power_limit(watt, self.T)
        self._oc_print(("✓ " if ok else "✗ ") + msg)
 
    def _apply_profile(self):
        sel = self._profile_list.curselection()
        if not sel:
            messagebox.showwarning(self._t("profile_title"), self._t("select_profile"))
            return
        key = self._profile_keys[sel[0]]
        results = self.ocmanager.apply_profile(key, self.T)
        for r in results:
            self._oc_print(r)
 
    def _show_profile_detail(self):
        sel = self._profile_list.curselection()
        if not sel:
            messagebox.showinfo(self._t("profile_title"), self._t("select_profile"))
            return
        key = self._profile_keys[sel[0]]
        p = self.ocmanager.get_profile(key)
        messagebox.showinfo(f"{self._t('profile_title')}: {key}", json.dumps(p, indent=2, ensure_ascii=False))
 
    def _build_report_tab(self, parent):
        btn_row = tk.Frame(parent, bg=C["bg"])
        btn_row.pack(fill="x", padx=20, pady=10)
        self._make_btn(btn_row, self._t("report_refresh"), self._refresh_report).pack(side="left")
        self._make_btn(btn_row, self._t("report_save"), self._save_report, C["green"]).pack(side="left", padx=8)
 
        self._report_txt = scrolledtext.ScrolledText(parent, font=FONT_MONO, fg=C["text"], bg=C["bg"],
                                                     bd=0, insertbackground=C["accent"])
        self._report_txt.pack(fill="both", expand=True, padx=20, pady=(0, 16))
        self._refresh_report()
 
    def _refresh_report(self):
        self._report_txt.config(state="normal")
        self._report_txt.delete("1.0", "end")
        self._report_txt.insert("1.0", self.sysinfo.full_report(self.T))
        self._report_txt.config(state="disabled")
 
    def _save_report(self):
        path = os.path.join(os.path.expanduser("~"), f"system_report_{datetime.now().strftime('%Y%m%d_%H%M%S')}.txt")
        with open(path, "w", encoding="utf-8") as f:
            f.write(self.sysinfo.full_report(self.T))
        messagebox.showinfo(self._t("saved_msg"), f"{self._t('report_saved')}:\n{path}")
 
    def _build_log_tab(self, parent):
        btn_row = tk.Frame(parent, bg=C["bg"])
        btn_row.pack(fill="x", padx=20, pady=10)
        self._make_btn(btn_row, self._t("log_clear"), self._clear_log).pack(side="left")
        self._make_btn(btn_row, self._t("log_save"), self._save_log, C["green"]).pack(side="left", padx=8)
 
        self._log_txt = scrolledtext.ScrolledText(parent, font=FONT_MONO, fg=C["dim"], bg=C["bg"],
                                                  bd=0, insertbackground=C["accent"])
        self._log_txt.pack(fill="both", expand=True, padx=20, pady=(0, 16))
        self._log_txt.insert("1.0", f"[{datetime.now().strftime('%H:%M:%S')}] {self._t('startup')}\n")
 
    def _clear_log(self):
        self._log_txt.delete("1.0", "end")
 
    def _save_log(self):
        path = os.path.join(os.path.expanduser("~"), f"sysoc_log_{datetime.now().strftime('%Y%m%d_%H%M%S')}.txt")
        with open(path, "w", encoding="utf-8") as f:
            f.write(self._log_txt.get("1.0", "end"))
        messagebox.showinfo(self._t("saved_msg"), f"{self._t('log_saved')}:\n{path}")
 
    def _start_live_update(self):
        def loop():
            while self._running:
                try:
                    self.after(0, self._update_live)
                    log_lines = self.ocmanager.log[:]
                    if log_lines:
                        self.after(0, lambda ll=log_lines: self._sync_log(ll))
                except Exception:
                    pass
                time.sleep(1.5)
        threading.Thread(target=loop, daemon=True).start()
 
    def _sync_log(self, lines: list):
        existing = self._log_txt.get("1.0", "end")
        for line in lines:
            if line and line not in existing:
                self._log_txt.insert("end", line + "\n")
                self._log_txt.see("end")
 
    def destroy(self):
        self._running = False
        super().destroy()
 
 
if __name__ == "__main__":
    app = SysOCApp()
    app.mainloop()


