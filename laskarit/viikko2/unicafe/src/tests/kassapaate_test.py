import unittest
from kassapaate import Kassapaate
from maksukortti import Maksukortti

class TestKassapaate(unittest.TestCase):
    def setUp(self):
        self.kassapaate = Kassapaate()


    def test_luotu_kassapaate_on_olemassa(self):
        self.assertNotEqual(self.kassapaate, None)
    
    def test_luodun_kassapaatteen_rahamäärä_on_oikea(self):
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)

    def test_luodun_kassapaatteen_myytyjen_edullisten_lounaiden_määrä_on_oikea(self):
        self.assertEqual(self.kassapaate.edulliset, 0)

    def test_luodun_kassapaatteen_myytyjen_maukkaiden_lounaiden_määrä_on_oikea(self):
        self.assertEqual(self.kassapaate.maukkaat, 0)




    # Käteismaksu, edullinen lounas:

    def test_jos_käteismaksu_riittävä_kassassa_oleva_rahamäärä_kasvaa_edullisen_lounaan_hinnalla(self):
        self.kassapaate.syo_edullisesti_kateisella(5000)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100240)
    
    def test_jos_käteismaksu_riittävä_edullisen_lounaan_vaihtorahan_suuruus_on_oikea(self):
        vaihtoraha = self.kassapaate.syo_edullisesti_kateisella(5000)
        self.assertEqual(vaihtoraha, 5000-240)

    def test_jos_käteismaksu_riittävä_myytyjen_edullisten_lounaiden_määrä_kasvaa(self):
        self.kassapaate.syo_edullisesti_kateisella(5000)
        self.assertEqual(self.kassapaate.edulliset, 1)

    def test_jos_edullisen_lounaan_käteismaksu_ei_riittävä_kassassa_oleva_rahamäärä_ei_kasva(self):
        self.kassapaate.syo_edullisesti_kateisella(100)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)
    
    def test_jos_edullisen_lounaan_käteismaksu_ei_riittävä_vaihtorahana_palautuu_koko_summa(self):
        vaihtoraha = self.kassapaate.syo_edullisesti_kateisella(100)
        self.assertEqual(vaihtoraha, 100)

    def test_jos_käteismaksu_ei_riittävä_myytyjen_edullisten_lounaiden_määrä_ei_kasva(self):
        self.kassapaate.syo_edullisesti_kateisella(100)
        self.assertEqual(self.kassapaate.edulliset, 0)



    
    # Käteismaksu, maukas lounas:  

    def test_jos_käteismaksu_riittävä_kassassa_oleva_rahamäärä_kasvaa_maukkaan_lounaan_hinnalla(self):
        self.kassapaate.syo_maukkaasti_kateisella(5000)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100400)
    
    def test_jos_käteismaksu_riittävä_maukkaan_lounaan_vaihtorahan_suuruus_on_oikea(self):
        vaihtoraha = self.kassapaate.syo_maukkaasti_kateisella(5000)
        self.assertEqual(vaihtoraha, 5000-400)

    def test_jos_käteismaksu_riittävä_myytyjen_maukkaiden_lounaiden_määrä_kasvaa(self):
        self.kassapaate.syo_maukkaasti_kateisella(5000)
        self.assertEqual(self.kassapaate.maukkaat, 1)

    def test_jos_maukkaan_lounaan_käteismaksu_ei_riittävä_kassassa_oleva_rahamäärä_ei_kasva(self):
        self.kassapaate.syo_maukkaasti_kateisella(100)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)
    
    def test_jos_maukkaan_lounaan_käteismaksu_ei_riittävä_vaihtorahana_palautuu_koko_summa(self):
        vaihtoraha = self.kassapaate.syo_maukkaasti_kateisella(100)
        self.assertEqual(vaihtoraha, 100)

    def test_jos_käteismaksu_ei_riittävä_myytyjen_maukkaiden_lounaiden_määrä_ei_kasva(self):
        self.kassapaate.syo_maukkaasti_kateisella(100)
        self.assertEqual(self.kassapaate.maukkaat, 0)

    


    # Korttiosto , edullinen lounas:
    def test_jos_saldo_riittävä_myytyjen_edullisten_lounaiden_määrä_kasvaa(self):
        maksukortti = Maksukortti(1000)
        self.kassapaate.syo_edullisesti_kortilla(maksukortti)
        self.assertEqual(self.kassapaate.edulliset, 1)
    
    def test_jos_saldo_riittävä_edullisen_lounaan_ostoon_palautetaan_True(self):
        maksukortti = Maksukortti(1000)
        palautus = self.kassapaate.syo_edullisesti_kortilla(maksukortti)
        self.assertEqual(palautus, True)

    def test_jos_saldo_riittävä_edullisen_lounaan_ostoon_veloitetaan_summa_kortilta(self):
        maksukortti = Maksukortti(1000)
        self.kassapaate.syo_edullisesti_kortilla(maksukortti)
        self.assertEqual(maksukortti.saldo, 1000-240)



    def test_jos_saldo_ei_riittävä_myytyjen_edullisten_lounaiden_määrä_ei_kasva(self):
        maksukortti = Maksukortti(100)
        self.kassapaate.syo_edullisesti_kortilla(maksukortti)
        self.assertEqual(self.kassapaate.edulliset, 0)
    
    def test_jos_saldo_ei_riittävä_edullisen_lounaan_ostoon_palautetaan_False(self):
        maksukortti = Maksukortti(100)
        palautus = self.kassapaate.syo_edullisesti_kortilla(maksukortti)
        self.assertEqual(palautus, False)

    def test_jos_saldo_ei_riittävä_edullisen_lounaan_ostoon_ei_veloiteta_korttia(self):
        maksukortti = Maksukortti(100)
        self.kassapaate.syo_edullisesti_kortilla(maksukortti)
        self.assertEqual(maksukortti.saldo, 100)

    

    # Korttiosto, maukas lounas:

    def test_jos_saldo_riittävä_myytyjen_maukkaiden_lounaiden_määrä_kasvaa(self):
        maksukortti = Maksukortti(1000)
        self.kassapaate.syo_maukkaasti_kortilla(maksukortti)
        self.assertEqual(self.kassapaate.maukkaat, 1)
    
    def test_jos_saldo_riittävä_maukkaan_lounaan_ostoon_palautetaan_True(self):
        maksukortti = Maksukortti(1000)
        palautus = self.kassapaate.syo_maukkaasti_kortilla(maksukortti)
        self.assertEqual(palautus, True)

    def test_jos_saldo_riittävä_maukkaan_lounaan_ostoon_veloitetaan_summa_kortilta(self):
        maksukortti = Maksukortti(1000)
        self.kassapaate.syo_maukkaasti_kortilla(maksukortti)
        self.assertEqual(maksukortti.saldo, 1000-400)


    def test_jos_saldo_ei_riittävä_myytyjen_maukkaiden_lounaiden_määrä_ei_kasva(self):
        maksukortti = Maksukortti(100)
        self.kassapaate.syo_maukkaasti_kortilla(maksukortti)
        self.assertEqual(self.kassapaate.maukkaat, 0)
    
    def test_jos_saldo_ei_riittävä_maukkaan_lounaan_ostoon_palautetaan_False(self):
        maksukortti = Maksukortti(100)
        palautus = self.kassapaate.syo_maukkaasti_kortilla(maksukortti)
        self.assertEqual(palautus, False)

    def test_jos_saldo_ei_riittävä_maukkaan_lounaan_ostoon_ei_veloiteta_korttia(self):
        maksukortti = Maksukortti(100)
        self.kassapaate.syo_maukkaasti_kortilla(maksukortti)
        self.assertEqual(maksukortti.saldo, 100)

    


    # Rahan lataus kortille:

    def test_kortille_rahaa_ladattaessa_kortin_saldo_muuttuu(self) :
        maksukortti = Maksukortti(100)
        self.kassapaate.lataa_rahaa_kortille(maksukortti, 100)
        self.assertEqual(maksukortti.saldo, 200)

    def test_kortille_rahaa_ladattaessa_kassassa_oleva_rahamäärä_kasvaa(self) :
        maksukortti = Maksukortti(100)
        self.kassapaate.lataa_rahaa_kortille(maksukortti, 100)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100100)

    def test_jos_kortille_yritetään_ladata_negatiivinen_summa_kortin_saldo_ei_muutu(self) :
        maksukortti = Maksukortti(100)
        self.kassapaate.lataa_rahaa_kortille(maksukortti, -100)
        self.assertEqual(maksukortti.saldo, 100)

    def test_os_kortille_yritetään_ladata_negatiivinen_summa_kassassa_oleva_rahamäärä_ei_kasva(self) :
        maksukortti = Maksukortti(100)
        self.kassapaate.lataa_rahaa_kortille(maksukortti, -100)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)
