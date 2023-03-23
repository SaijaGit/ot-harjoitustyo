import unittest
from maksukortti import Maksukortti

class TestMaksukortti(unittest.TestCase):
    def setUp(self):
        self.maksukortti = Maksukortti(1000)

    def test_luotu_kortti_on_olemassa(self):
        self.assertNotEqual(self.maksukortti, None)

    
    def test_konstruktori_asettaa_saldon_oikein(self):
        self.assertEqual(str(self.maksukortti), "Kortilla on rahaa 10.00 euroa")
    
    
    def test_rahan_lataaminen_kasvattaa_saldoa_oikein(self):
        self.maksukortti.lataa_rahaa(2500)
        self.assertEqual(str(self.maksukortti), "Kortilla on rahaa 35.00 euroa")


    def test_rahan_ottaminen_vahentaa_saldoa_oikein_jos_rahaa_on_tarpeeksi(self):
        self.maksukortti.ota_rahaa(500)
        self.assertEqual(str(self.maksukortti), "Kortilla on rahaa 5.00 euroa")


    def test_rahan_ottaminen_ei_muuta_saldoa_jos_rahaa_ei_ole_tarpeeksi(self):
        self.maksukortti.ota_rahaa(5000)
        self.assertEqual(str(self.maksukortti), "Kortilla on rahaa 10.00 euroa")


    def test_rahan_ottaminen_palauttaa_True_jos_rahat_riittivät(self):
        palautus = self.maksukortti.ota_rahaa(500)
        self.assertEqual(palautus, True)


    def test_rahan_ottaminen_palauttaa_False_jos_rahat_eivät_riitä(self):
        palautus = self.maksukortti.ota_rahaa(5000)
        self.assertEqual(palautus, False)



