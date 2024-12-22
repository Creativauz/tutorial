#sample database untuk tutorial di blog Creativauz
class DataMarketing(models.Model):
    nama_marketing = models.CharField(max_length=200, blank=True, null=True)
    email_marketing = models.CharField(max_length=200, blank=True, null=True)
    alamat_marketing = models.CharField(max_length=200, blank=True, null=True)
    no_hp = models.CharField(max_length=200, blank=True, null=True)

class DataPelanggan(models.Model):
    ALAMAT_CHOICES = [
        ('alamat_1', 'Alamat 1'),
        ('alamat_2', 'Alamat 2'),
        ('alamat_3', 'Alamat 3'),
    ]
    PILIH_STATUS_PAYMENT = [
        ('Paid', 'Paid'),
        ('Unpaid', 'Unpaid'),
        ('Termin', 'Termin'),
    ]
    tanggal_subscribe = models.DateTimeField(null=True, blank=True)
    subscribe_berakhir = models.DateTimeField(null=True, blank=True)
    nama_pelanggan = models.CharField(max_length=200)
    no_hp = models.PositiveIntegerField()
    email = models.EmailField(max_length=200)
    alamat_1 = RichTextField()
    alamat_2 = RichTextField(null=True, blank=True)
    alamat_3 = RichTextField(null=True, blank=True)
    alamat_default = models.CharField(max_length=10, choices=ALAMAT_CHOICES, default='alamat_1')
    harga = models.PositiveIntegerField()
    paket_yang_dipesan = models.ForeignKey('PaketPelanggan', on_delete=models.CASCADE)
    leads_by = models.ForeignKey(DataMarketing, on_delete=models.CASCADE, null=True, blank=True)
    status_pembayaran = models.CharField(max_length=20, choices=PILIH_STATUS_PAYMENT, default='Unpaid')
    bayar_lunas = models.PositiveIntegerField(null=True, blank=True)
    bukti_trf_paid = models.ImageField(upload_to='bukti_trf/paid/', null=True, blank=True)
    jumlah_termin = models.PositiveIntegerField(null=True, blank=True)
    bukti_trf_termin = models.ImageField(upload_to='bukti_trf/termin/', null=True, blank=True)
    qty = models.PositiveIntegerField(null=True, blank=True)
    diskon = models.PositiveIntegerField(null=True, blank=True)
    status_langganan = models.BooleanField(default=False)
    batch = models.PositiveIntegerField(default=0, help_text="Menyimpan jumlah perpanjangan langganan")
    cuti = models.BooleanField(default=False)
    mulai_cuti = models.DateTimeField(null=True, blank=True)
    akhir_cuti = models.DateTimeField(null=True, blank=True)
    ref_by = models.ForeignKey(ReferralUser, on_delete=models.CASCADE, null=True, blank=True)
	
class Pembayaran(models.Model):
    pelanggan = models.ForeignKey(DataPelanggan, on_delete=models.CASCADE, related_name="pembayaran")
    batch = models.PositiveIntegerField()
    jumlah = models.PositiveIntegerField()	