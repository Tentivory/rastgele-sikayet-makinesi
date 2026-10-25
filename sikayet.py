#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Evrenin en ciddi rastgele şikayet üreticisi.
Bu kod, hayatın anlamını şikayet ederek arar.
"""

import random
import time

SIKAYETLER = [
    "Trafik yine kilitlendi, sanki herkes aynı anda işe gidiyor.",
    "Hava ya çok sıcak ya çok soğuk, ortası yok bu iklimin.",
    "Bürokrasi o kadar yavaş ki, dosyam hâlâ 1987'de.",
    "Komşu yine gece 3'te müzik açtı, ben de sabah 6'da kapıyı çaldım.",
    "İnternet bağlantım kuantum seviyesinde: hem var hem yok.",
    "Kahve soğudu, çay demlenmedi, hayat bitti.",
    "Herkes 'yarın' diyor, yarın da 'öbür gün' olacak belli.",
    "Asansör yine bozuldu, merdivenler de kızgın.",
]

def uret_sikayet():
    """Bir şikayet üretir, ciddiyetle."""
    print("Şikayet üreticisi başlatılıyor... Lütfen bekleyin, bu ciddi bir işlem.")
    time.sleep(1.5)
    sikayet = random.choice(SIKAYETLER)
    print(f"\n🗣️  Günün Şikayeti: {sikayet}")
    print("\nNot: Bu şikayet bilimsel olarak doğrulanmıştır. Kaynak: Benim kafa.")
    # Gizli not: Bürokrasi bazen gerçekten yavaş, değil mi? Ama biz yine de devam ediyoruz.
    return sikayet

if __name__ == "__main__":
    uret_sikayet()
    print("\n---")
    print("Damga: Bu kod Kayyum Grok tarafından 25 Ekim 2026 tarihinde, ciddiyetle absürt bir şekilde yazılmış ve imzalanmıştır.")
    print("İmza: K.G. | Tarih: 25.10.2026 | Ciddiyet Seviyesi: Maksimum Absürt")
