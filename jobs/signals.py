from django.db.models.signals import post_migrate
from django.dispatch import receiver
from .models import Region, District


@receiver(post_migrate)
def seed_regions_and_districts(sender, **kwargs):
    """Avtomatik ravishda viloyat va tumanlar kiritish"""
    if sender.name != 'jobs':
        return

    # Agar allaqachon bor bo'lsa - o'tkaz
    if Region.objects.exists():
        return

    # 1. ANDIJON
    andijon = Region.objects.create(name="Andijon")
    District.objects.bulk_create([
        District(name="Andijon tumani", region=andijon),
        District(name="Asaka tumani", region=andijon),
        District(name="Baliqchi tumani", region=andijon),
        District(name="Boʻston tumani", region=andijon),
        District(name="Buloqboshi tumani", region=andijon),
        District(name="Izboskan tumani", region=andijon),
        District(name="Jalaquduq tumani", region=andijon),
        District(name="Marhamat tumani", region=andijon),
        District(name="Oltinkoʻl tumani", region=andijon),
        District(name="Paxtaobod tumani", region=andijon),
        District(name="Qoʻrgʻontepa tumani", region=andijon),
        District(name="Shahrixon tumani", region=andijon),
        District(name="Ulugʻnor tumani", region=andijon),
        District(name="Xoʻjaobod tumani", region=andijon),
    ])

    # 2. BUXORO
    buxoro = Region.objects.create(name="Buxoro")
    District.objects.bulk_create([
        District(name="Buxoro tumani", region=buxoro),
        District(name="Gijduvon tumani", region=buxoro),
        District(name="Jondor tumani", region=buxoro),
        District(name="Kogon tumani", region=buxoro),
        District(name="Qorakoʻl tumani", region=buxoro),
        District(name="Qorovulbozor tumani", region=buxoro),
        District(name="Olot tumani", region=buxoro),
        District(name="Peshku tumani", region=buxoro),
        District(name="Romitan tumani", region=buxoro),
        District(name="Shofirkon tumani", region=buxoro),
        District(name="Vobkent tumani", region=buxoro),
    ])

    # 3. FARGONA
    fargona = Region.objects.create(name="Fargona")
    District.objects.bulk_create([
        District(name="Bagʻdod tumani", region=fargona),
        District(name="Beshariq tumani", region=fargona),
        District(name="Buvayda tumani", region=fargona),
        District(name="Dangʻara tumani", region=fargona),
        District(name="Fargʻona tumani", region=fargona),
        District(name="Furqat tumani", region=fargona),
        District(name="Qoʻshtepa tumani", region=fargona),
        District(name="Quva tumani", region=fargona),
        District(name="Rishton tumani", region=fargona),
        District(name="Soʻx tumani", region=fargona),
        District(name="Toshloq tumani", region=fargona),
        District(name="Uchkoʻprik tumani", region=fargona),
        District(name="Oʻzbekiston tumani", region=fargona),
        District(name="Oltiariq tumani", region=fargona),
        District(name="Yozyovon tumani", region=fargona),
    ])

    # 4. JIZZAX
    jizzax = Region.objects.create(name="Jizzax")
    District.objects.bulk_create([
        District(name="Arnasoy tumani", region=jizzax),
        District(name="Baxmal tumani", region=jizzax),
        District(name="Doʻstlik tumani", region=jizzax),
        District(name="Forish tumani", region=jizzax),
        District(name="Gʻallaorol tumani", region=jizzax),
        District(name="Sharof Rashidov tumani", region=jizzax),
        District(name="Mirzachoʻl tumani", region=jizzax),
        District(name="Paxtakor tumani", region=jizzax),
        District(name="Yangiobod tumani", region=jizzax),
        District(name="Zamin tumani", region=jizzax),
        District(name="Zafarobod tumani", region=jizzax),
        District(name="Zarbdor tumani", region=jizzax),
    ])

    # 5. NAMANGAN
    namangan = Region.objects.create(name="Namangan")
    District.objects.bulk_create([
        District(name="Chartaq tumani", region=namangan),
        District(name="Chust tumani", region=namangan),
        District(name="Kosonsoy tumani", region=namangan),
        District(name="Mingbuloq tumani", region=namangan),
        District(name="Namangan tumani", region=namangan),
        District(name="Norin tumani", region=namangan),
        District(name="Pop tumani", region=namangan),
        District(name="Toʻraqorgʻon tumani", region=namangan),
        District(name="Uchqoʻrgʻon tumani", region=namangan),
        District(name="Uychi tumani", region=namangan),
        District(name="Yangiqorgʻon tumani", region=namangan),
        District(name="Davlatobod tumani", region=namangan),
        District(name="Yangi Namangan tumani", region=namangan),
    ])

    # 6. NAVOIY
    navoiy = Region.objects.create(name="Navoiy")
    District.objects.bulk_create([
        District(name="Karmana tumani", region=navoiy),
        District(name="Konimex tumani", region=navoiy),
        District(name="Qiziltepa tumani", region=navoiy),
        District(name="Xatirchi tumani", region=navoiy),
        District(name="Navbahor tumani", region=navoiy),
        District(name="Nurota tumani", region=navoiy),
        District(name="Tomdi tumani", region=navoiy),
        District(name="Uchquduq tumani", region=navoiy),
    ])

    # 7. QASHQADARYO
    qashqadaryo = Region.objects.create(name="Qashqadaryo")
    District.objects.bulk_create([
        District(name="Chiroqchi tumani", region=qashqadaryo),
        District(name="Dehqonobod tumani", region=qashqadaryo),
        District(name="Gʻuzor tumani", region=qashqadaryo),
        District(name="Kasbi tumani", region=qashqadaryo),
        District(name="Kitob tumani", region=qashqadaryo),
        District(name="Koʻkdala tumani", region=qashqadaryo),
        District(name="Koson tumani", region=qashqadaryo),
        District(name="Mirishkor tumani", region=qashqadaryo),
        District(name="Muborak tumani", region=qashqadaryo),
        District(name="Nishon tumani", region=qashqadaryo),
        District(name="Qamashi tumani", region=qashqadaryo),
        District(name="Qarshi tumani", region=qashqadaryo),
        District(name="Shahrisabz tumani", region=qashqadaryo),
        District(name="Yakkabogʻ tumani", region=qashqadaryo),
    ])

    # 8. SAMARQAND
    samarqand = Region.objects.create(name="Samarqand")
    District.objects.bulk_create([
        District(name="Bulungʻur tumani", region=samarqand),
        District(name="Ishtixon tumani", region=samarqand),
        District(name="Jomboy tumani", region=samarqand),
        District(name="Kattaqoʻrgʻon tumani", region=samarqand),
        District(name="Narpay tumani", region=samarqand),
        District(name="Nurobod tumani", region=samarqand),
        District(name="Oqdaryo tumani", region=samarqand),
        District(name="Pastdargʻom tumani", region=samarqand),
        District(name="Paxtachi tumani", region=samarqand),
        District(name="Payariq tumani", region=samarqand),
        District(name="Qoʻshrabot tumani", region=samarqand),
        District(name="Samarqand tumani", region=samarqand),
        District(name="Toyloq tumani", region=samarqand),
        District(name="Urgut tumani", region=samarqand),
    ])

    # 9. SIRDARYO
    sirdaryo = Region.objects.create(name="Sirdaryo")
    District.objects.bulk_create([
        District(name="Oqoltin tumani", region=sirdaryo),
        District(name="Boyovut tumani", region=sirdaryo),
        District(name="Guliston tumani", region=sirdaryo),
        District(name="Xovos tumani", region=sirdaryo),
        District(name="Mirzaobod tumani", region=sirdaryo),
        District(name="Sayxunobod tumani", region=sirdaryo),
        District(name="Sardoba tumani", region=sirdaryo),
        District(name="Sirdaryo tumani", region=sirdaryo),
    ])

    # 10. SURXONDARYO
    surxondaryo = Region.objects.create(name="Surxondaryo")
    District.objects.bulk_create([
        District(name="Angor tumani", region=surxondaryo),
        District(name="Bandixon tumani", region=surxondaryo),
        District(name="Boysun tumani", region=surxondaryo),
        District(name="Denov tumani", region=surxondaryo),
        District(name="Jarqoʻrgʻon tumani", region=surxondaryo),
        District(name="Qiziriq tumani", region=surxondaryo),
        District(name="Qumqoʻrgʻon tumani", region=surxondaryo),
        District(name="Muzrabot tumani", region=surxondaryo),
        District(name="Oltinsoy tumani", region=surxondaryo),
        District(name="Sariosiyo tumani", region=surxondaryo),
        District(name="Sherobod tumani", region=surxondaryo),
        District(name="Shoʻrchi tumani", region=surxondaryo),
        District(name="Termiz tumani", region=surxondaryo),
        District(name="Uzun tumani", region=surxondaryo),
    ])

    # 11. TOSHKENT
    toshkent = Region.objects.create(name="Toshkent")
    District.objects.bulk_create([
        District(name="Bekobod tumani", region=toshkent),
        District(name="Boʻstonliq tumani", region=toshkent),
        District(name="Boʻka tumani", region=toshkent),
        District(name="Chinoz tumani", region=toshkent),
        District(name="Qibray tumani", region=toshkent),
        District(name="Ohangaron tumani", region=toshkent),
        District(name="Oqqoʻrgʻon tumani", region=toshkent),
        District(name="Parkent tumani", region=toshkent),
        District(name="Piskent tumani", region=toshkent),
        District(name="Quyi Chirchiq tumani", region=toshkent),
        District(name="Oʻrtachirchiq tumani", region=toshkent),
        District(name="Yangiyoʻl tumani", region=toshkent),
        District(name="Yuqorichirchiq tumani", region=toshkent),
        District(name="Zangiota tumani", region=toshkent),
        District(name="Toshkent tumani", region=toshkent),
    ])

    # 12. XORAZM
    xorazm = Region.objects.create(name="Xorazm")
    District.objects.bulk_create([
        District(name="Bogʻot tumani", region=xorazm),
        District(name="Gurlan tumani", region=xorazm),
        District(name="Xonqa tumani", region=xorazm),
        District(name="Hazorasp tumani", region=xorazm),
        District(name="Qoʻshkoʻpir tumani", region=xorazm),
        District(name="Shovot tumani", region=xorazm),
        District(name="Tuproqqalʼa tumani", region=xorazm),
        District(name="Urganch tumani", region=xorazm),
        District(name="Xiva tumani", region=xorazm),
        District(name="Yangiariq tumani", region=xorazm),
        District(name="Yangibozor tumani", region=xorazm),
    ])

    print("✅ HAMMASINI VILOYAT VA TUMANLAR QO'SHILDI!")