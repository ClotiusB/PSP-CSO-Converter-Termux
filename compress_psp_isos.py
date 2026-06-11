#!/usr/bin/env python3

import subprocess
from pathlib import Path

ISO_DIR = Path("/sdcard/Download/PSP-Iso")
CSO_DIR = Path("/sdcard/Download/PSP-Cso")

COMP_LEVEL = "9"

TRANSLATIONS = {
    "pt_BR": {
        "iso_handling_title": "PREFERENCIA DE TRATAMENTO ISO",
        "iso_option_1": "[1] Manter arquivos ISO apos compressao",
        "iso_option_2": "[2] Remover arquivos ISO apos compressao",

        "starting": "INICIANDO COMPRESSAO",
        "processing": "Processando",
        "success": "Conversao concluida",
        "failed": "Falha na conversao",

        "summary": "RESUMO FINAL",
        "found": "ISOs encontradas",
        "converted": "Convertidas",
        "failed_count": "Falhadas/Puladas",

        "iso_size": "Tamanho ISO",
        "cso_size": "Tamanho CSO",
        "reduction": "Reducao",

        "no_iso": "Nenhum arquivo ISO encontrado.",
        "dirs_ready": "Pastas PSP-Iso e PSP-Cso verificadas.",

        "skip_exists": "Arquivo CSO ja existe."
    },

    "en_US": {
        "iso_handling_title": "ISO HANDLING PREFERENCE",
        "iso_option_1": "[1] Keep ISO files after compression",
        "iso_option_2": "[2] Remove ISO files after compression",

        "starting": "STARTING COMPRESSION",
        "processing": "Processing",
        "success": "Conversion completed",
        "failed": "Conversion failed",

        "summary": "SUMMARY",
        "found": "ISOs found",
        "converted": "Converted",
        "failed_count": "Failed/Skipped",

        "iso_size": "ISO Size",
        "cso_size": "CSO Size",
        "reduction": "Reduction",

        "no_iso": "No ISO files found.",
        "dirs_ready": "PSP-Iso and PSP-Cso directories verified.",

        "skip_exists": "CSO file already exists."
    }
}


def t(key, lang):
    return TRANSLATIONS[lang][key]


def clear_screen():
    subprocess.run(["clear"], check=False)


def format_size(size):
    for unit in ["B", "KB", "MB", "GB"]:
        if size < 1024:
            return f"{size:.2f} {unit}"
        size /= 1024
    return f"{size:.2f} TB"


def get_language():
    while True:
        clear_screen()

        print("==================================================")
        print(" LANGUAGE / IDIOMA ")
        print("==================================================")
        print()
        print("[1] Português Brasileiro")
        print("[2] English (American)")
        print()

        choice = input("> ").strip()

        if choice == "1":
            return "pt_BR"

        if choice == "2":
            return "en_US"


def keep_iso_menu(lang):
    while True:
        clear_screen()

        print("==================================================")
        print(t("iso_handling_title", lang))
        print("==================================================")
        print()

        print(t("iso_option_1", lang))
        print(t("iso_option_2", lang))
        print()

        choice = input("> ").strip()

        if choice == "1":
            return True

        if choice == "2":
            return False


def main():
    lang = get_language()

    ISO_DIR.mkdir(parents=True, exist_ok=True)
    CSO_DIR.mkdir(parents=True, exist_ok=True)

    clear_screen()
    print(t("dirs_ready", lang))

    keep_iso = keep_iso_menu(lang)

    iso_files = sorted(ISO_DIR.glob("*.iso"))

    if not iso_files:
        clear_screen()
        print(t("no_iso", lang))
        return

    clear_screen()

    print("==================================================")
    print(t("starting", lang))
    print("==================================================")
    print()

    results = []
    converted = 0

    total_files = len(iso_files)

    for index, iso in enumerate(iso_files, start=1):

        clear_screen()

        game = iso.stem
        cso_file = CSO_DIR / f"{game}.cso"

        if cso_file.exists():
            print("==================================================")
            print(
                f"[{index}/{total_files}] "
                f"{t('processing', lang)}: {iso.name}"
            )
            print("==================================================")
            print()
            print(t("skip_exists", lang))
            print()
            continue

        print("==================================================")
        print(
            f"[{index}/{total_files}] "
            f"{t('processing', lang)}: {iso.name}"
        )
        print("==================================================")
        print()

        iso_size = iso.stat().st_size

        cmd = [
            "ciso",
            COMP_LEVEL,
            str(iso),
            str(cso_file)
        ]

        result = subprocess.run(
            cmd,
            stdout=subprocess.DEVNULL,
            stderr=subprocess.DEVNULL
        )

        if result.returncode != 0:
            print(t("failed", lang))
            input("\nPress Enter...")
            continue

        if not cso_file.exists():
            print(t("failed", lang))
            input("\nPress Enter...")
            continue

        cso_size = cso_file.stat().st_size

        if not keep_iso:
            iso.unlink()

        reduction = ((iso_size - cso_size) / iso_size) * 100

        results.append({
            "name": game,
            "iso": iso_size,
            "cso": cso_size,
            "reduction": reduction
        })

        converted += 1

        print(t("success", lang))
        print()

    clear_screen()

    print("==================================================")
    print(t("summary", lang))
    print("==================================================")

    print(f"{t('found', lang)}: {len(iso_files)}")
    print(f"{t('converted', lang)}: {converted}")
    print(f"{t('failed_count', lang)}: {len(iso_files) - converted}")

    print()

    for game in results:

        print(game["name"])

        print(
            f"  {t('iso_size', lang)}: "
            f"{format_size(game['iso'])}"
        )

        print(
            f"  {t('cso_size', lang)}: "
            f"{format_size(game['cso'])}"
        )

        print(
            f"  {t('reduction', lang)}: "
            f"{game['reduction']:.2f}%"
        )

        print()


if __name__ == "__main__":
    main()
      
