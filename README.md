
[pgm images](https://people.sc.fsu.edu/~jburkardt/data/pgma/pgma.html)

## 2. óra
1. [x] Hisztogram-kiegyenlítés szürkeskálás képeken (a képek beolvasása és kiírása is része a feladatnak, képformátum: pgm)

2. [x] Átlagoló szűrő szürkeskálás képeken (a képek beolvasása és kiírása is része a feladatnak, a képformátum: pgm). A program paramétere a sablon mérete: 3x3, 5x5 vagy 7x7, illetve a hiányzó pozíciók értelmezése: csak teljes illeszkedés van, hiányzó elemek nullák, hiányzó elemek kimaradnak.

3. [x] Medián szűrő szürkeskálás képeken (a képek beolvasása és kiírása is része a feladatnak, a képformátum: pgm). A program paramétere a sablon mérete: 3x3, 5x5 vagy 7x7, illetve a hiányzó pozíciók értelmezése: csak teljes illeszkedés van, hiányzó elemek nullák, hiányzó elemek kimaradnak.

4. [x] Képek átlagolása és mediánja (a képek beolvasása és kiírása is része a feladatnak, a képformátum: pgm).

5. [x] Küszöbölés szűrkeskálás képeken (a képek beolvasása és kiírása is része a feladatnak, a képformátum: pgm)

## 3. óra
6. [x] Morfológiai operátor (erózió, dilatáció, nyitás vagy zárás). Csak egyet kell megvalósítani. A képek beolvasására és kimentésére lehet használni az OpenCV függvényeket.

7. [x] Hit-or-Miss transzformáció. A képek beolvasására és kimentésére lehet használni az OpenCV függvényeket.

8. [x] Szürkeskálás dilatáció és erózió. A képek beolvasására és kimentésére lehet használni az OpenCV függvényeket.

## 4. óra
9. [x] Fourier-transzformáció és annak inverzének kiszámítása. Bemenő adat egy max. 15x15-ös mátrix, amelynek elemei 8 bites nemnegatív egész számok. A kimenet a számítás eredményét tartalmazó mátrix.

## 5. óra
10. [x] Frekvenciatérbeli szűrés az ILPF és IHPF segítségével. A bemenő adat a kép mellett a vágási frekvencia. A szűrés kivételével használható az OpenCV függvénykönyvtár.

11. [x] Frekvenciatérbeli szűrés az IBPF és IBSF segítségével. A bemenő adat a kép mellett a két vágási frekvencia. A szűrés kivételével használható az OpenCV függvénykönyvtár.

12. [ ] Szűrők összehasonlítása. Az ILPF, BLPF és GLPF, illetve a IHPF, BHPF és GHPF összehasonlítása páronkénti különbségképek segítségével. Az OpenCV függvénykönyvtár minden függvénye használható.

13. [ ] Szűrők összehasonlítása. Az IBPF, BBPF és GBPF, illetve a IBSF, BBSF és GBSF összehasonlítása páronkénti különbségképek segítségével. Az OpenCV függvénykönyvtár minden függvénye használható.

## 6. óra
14. [x] Sablonozás alapú éldetektor megvalósítása. OpenCV minden függvénye használható, kivéve az éldetektorokat.

15. [x] Három éldetektor kiválasztása, aminek az eredményeit kell páronként összehasonlítani. Az OpenCV bármilyen függvénye használható.

## 7. óra

16. [x] Hough-transzformáció alkalmazása téglalap irányának meghatározására.

17. [x] Tetszőleg vázkijelölő módszer implementálása.


### how to a install dependencies in virtual environment? 
```python
python3 -m venv venv
pip3 install numpy
```