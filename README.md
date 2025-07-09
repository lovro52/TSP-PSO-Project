# 🛫 TSP – Particle Swarm Optimization (PSO)

## Opis problema

Ovaj projekt koristi **Particle Swarm Optimization (PSO)** algoritam za rješavanje **problema trgovačkog putnika (TSP)** za 50 stvarnih europskih gradova. Cilj je pronaći najkraću moguću rutu koja posjećuje sve gradove točno jednom i vraća se na početak. Gradovi su definirani geografskim koordinatama (latituda i longituda), a udaljenosti se računaju **Haversine formulom**.

---

## Struktura projekta

```
.
├── data/
│   └── coords.csv                 # Gradovi s koordinatama
├── results/
│   ├── best_distance.txt         # Najbolja ukupna udaljenost i ruta
│   └── route_plot.png            # Vizualizacija najbolje rute
├── src/
│   └── tsp_pso.py                # Glavna Python skripta s PSO implementacijom
├── venv/                         # Virtualno okruženje (ne uključuje se u Git)
├── requirements.txt             # Ovisnosti
├── README.md                    # Dokumentacija
└── .gitignore                   # Ignorirane datoteke za Git
```

---

## Pokretanje projekta

### 1. Kloniranje repozitorija

```bash
git clone https://github.com/tvoje-ime/TSP-PSO.git
cd TSP-PSO
```

### 2. Postavljanje virtualnog okruženja (preporučeno)

```bash
python -m venv venv
venv\Scripts\activate      # Windows
# ili
source venv/bin/activate     # Linux/macOS
```

### 3. Instalacija ovisnosti

```bash
pip install -r requirements.txt
```

### 4. Pokretanje koda

```bash
python src/tsp_pso.py
```

---

## Ulazni podaci

- `data/coords.csv`: CSV datoteka s gradovima i njihovim koordinatama  
  Kolone: `City`, `Latitude`, `Longitude`

---

## Izlazni rezultati

- `results/route_plot.png`: Vizualizacija rute (putanja kroz sve gradove)
- `results/best_distance.txt`: Ukupna duljina rute i redoslijed obilaska
- Terminal: Prikaz imena gradova redom kako su posjećeni

---

## Parametri PSO algoritma

| Parametar      | Vrijednost                                  |
| -------------- | ------------------------------------------- |
| Broj čestica   | 50                                          |
| Broj iteracija | 500                                         |
| Mutacija       | Swap (nasumične zamjene 2 grada po čestici) |
| Funkcija cilja | Zbroj Haversine udaljenosti između gradova  |

---

## Primjer izlaza (terminal)

```
Najbolja udaljenost: 11842.73 km

Redoslijed obilaska gradova:
- Paris
- Amsterdam
- Brussels
- Berlin
...
```

---

## Implementirane funkcionalnosti

- Računanje udaljenosti Haversine formulom
- Matrica udaljenosti među svim gradovima
- PSO s permutacijama i lokalnim/globalnim minimumom
- Vizualizacija rezultata pomoću matplotliba
- Spremanje rezultata u `results/`

---

## 📚 Usporedba s referencom

Projekt koristi osnovni princip PSO algoritma preuzet iz:
[Particle Swarm Optimization – Python Implementation](https://medium.com/@yahiazakaria445/particle-swarm-optimization-pso-algorithm-in-python-9960a1858435)

### 🔄 Prilagodbe napravljene za TSP:

| Element         | Referentni kod                 | Ovaj projekt                        |
| --------------- | ------------------------------ | ----------------------------------- |
| Tip problema    | Kontinuirani (realni brojevi)  | Diskretni (permutacije gradova)     |
| Reprezentacija  | Vektor vrijednosti (x ∈ ℝⁿ)    | Permutacija indeksa gradova         |
| Funkcija cilja  | `sum(x**2)` (Sphere)           | Zbroj Haversine udaljenosti po ruti |
| Mutacija/Update | Standardna PSO formula (v + x) | Swap mutacija permutacija           |
| Rezultat        | Najmanja vrijednost funkcije   | Najkraća ruta i udaljenost u km     |

Naš projekt je **praktična primjena PSO-a na realni problem (TSP)**, pri čemu smo algoritam iz reference prilagodili za rad s diskretnim prostorom rješenja i geografskim udaljenostima.

---

## Autor

Lovro Luka Matan
Fakultet informatike u Puli
Predmet: Robotika  
2025.
