import random

class Player:
    def __init__(self, stats):
        self.stats = stats  # Słownik ze statystykami gracza (np. zdrowie, ochrona itp.)
        self.time_multiplier = 1  
        self.hunting_xp = 0  # Doświadczenie polowania
        self.exploration_xp = 0  # Doświadczenie eksploracji
        self.inventory = []  # Tymczasowy ekwipunek gracza
        
    def take_damage(self, amount):
        """Zmniejsza zdrowie gracza o podaną wartość i sprawdza, czy gracz żyje."""
        self.stats['Zdrowie'] -= amount
        if self.stats['Zdrowie'] <= 0:
            self.stats['Zdrowie'] = 0
            print("Gracz zginął. Koniec gry.")
        else:
            print(f"Gracz otrzymał {amount} obrażeń. Zdrowie: {self.stats['Zdrowie']}/{self.stats['max_health']}")

    def heal(self, amount):
        """Regeneruje zdrowie gracza o podaną wartość, ale nie przekracza maksymalnego zdrowia."""
        self.stats['Zdrowie'] += amount
        if self.stats['Zdrowie'] > self.stats['max_health']:
            self.stats['Zdrowie'] = self.stats['max_health']
        print(f"Gracz odzyskał {amount} zdrowia. Zdrowie: {self.stats['Zdrowie']}/{self.stats['max_health']}")

    def calculate_temperature(self, ambient_temperature, clothing, is_near_fire):
        """Oblicza efektywną temperaturę otoczenia na podstawie różnych czynników."""
        protection = sum(clothing.values())
        fire_bonus = 10 if is_near_fire else 0

        effective_temperature = ambient_temperature + protection + fire_bonus
        print(f"Efektywna temperatura otoczenia: {effective_temperature}°C")

        return effective_temperature
    def reduce_stamina(self, amount):
        """Zmniejsza poziom staminy gracza po wykonaniu akcji."""
        self.stats['stamina'] -= amount
        if self.stats['stamina'] < 0:
            self.stats['stamina'] = 0
            print("Gracz stracił przytomność z powodu wyczerpania i musi odpocząć!")
            self.forced_rest()
        elif self.stats['stamina'] < self.stats['max_stamina'] * 0.25:
            print("Gracz jest zmęczony, akcje zajmują więcej czasu.")
            self.time_multiplier = 2  # --- ZMIANA MNOŻNIKA CZASU ---
        else:
            self.time_multiplier = 1  # --- RESET MNOŻNIKA CZASU ---
        print(f"Gracz stracił {amount} staminy. Stamina: {self.stats['stamina']}/{self.stats['max_stamina']}")

    def restore_stamina(self, amount, forced=False):
        """Odnawia staminę gracza podczas odpoczynku lub snu."""
        if forced:
            amount /= 2  # Wymuszony odpoczynek odzyskuje mniej staminy
        self.stats['stamina'] += amount
        if self.stats['stamina'] > self.stats['max_stamina']:
            self.stats['stamina'] = self.stats['max_stamina']
        print(f"Gracz odzyskał {amount} staminy. Stamina: {self.stats['stamina']}/{self.stats['max_stamina']}")
        if self.stats['stamina'] >= self.stats['max_stamina'] * 0.25:
            self.time_multiplier = 1  # --- RESET MNOŻNIKA CZASU PO ODZYSKANIU STAMINY ---
    
    def forced_rest(self):
        """Gracz traci przytomność i zostaje zmuszony do odpoczynku."""
        self.restore_stamina(self.stats['max_stamina'] * 0.5, forced=True)
    def explore(self, location):
        """Przeprowadza eksplorację i przyznaje łupy odpowiednie dla danej lokalizacji."""
        loot_table = {
            "urban": loot_table_urban_exploration,
            "forest": loot_table_forest_exploration,
            "hunting": loot_table_hunting_exploration
        }.get(location, [])
        
        print(f"Gracz eksploruje {location}...")
        for item, chance in loot_table:
            if random.randint(1, 100) <= chance:
                self.inventory.append(item)
                print(f"Znaleziono: {item}")

    def hunt(self, location):
        """Przeprowadza polowanie i przyznaje łupy odpowiednie dla danej lokalizacji."""
        loot_table = {
            "urban": loot_table_urban_hunting,
            "forest": loot_table_forest_hunting,
            "hunting": loot_table_hunting_hunting
        }.get(location, [])

        print(f"Gracz poluje w {location}...")
        for item, chance in loot_table:
            if random.randint(1, 100) <= chance:
                self.inventory.append(item)
                print(f"Znaleziono: {item}")

# Przykład użycia z zewnętrznymi danymi o ubraniach
if __name__ == "__main__":
    # Dane o ubraniach z poziomami ochrony
    clothing_data = {
        "jacket": {"level_1": 20, "level_2": 30, "level_3": 40},
        "boots": {"level_1": 10, "level_2": 20, "level_3": 30},
        "gloves": {"level_1": 5, "level_2": 10, "level_3": 15},
        "hat": {"level_1": 10, "level_2": 15, "level_3": 20}
    }

    # Statystyki gracza
    player_stats = {
        'health': 100,
        'max_health': 100,
        'stamina': 100,  
        'max_stamina': 100 
    }

    player = Player(stats=player_stats)

    # Gracz zakłada ubrania na poziomie 2
    equipped_clothing = {
        "jacket": clothing_data["jacket"]["level_2"],
        "boots": clothing_data["boots"]["level_2"],
        "gloves": clothing_data["gloves"]["level_2"],
        "hat": clothing_data["hat"]["level_2"]
    }

    # Symulacja temperatury w lesie zimowym
    ambient_temperature = -10.0  # Temperatura otoczenia w °C
    is_near_fire = False  # Czy gracz jest przy ognisku

    for _ in range(10):
        effective_temp = player.calculate_temperature(ambient_temperature, equipped_clothing, is_near_fire)
        if effective_temp < 0:
            player.take_damage(5)  # Obrażenia za wychłodzenie
            player.reduce_stamina(5)  # --- Utrata staminy za przebywanie w zimnie ---

    # Gracz ogrzewa się przy ognisku
    print("Gracz zbliża się do ogniska...")
    is_near_fire = True
    for _ in range(5):
        effective_temp = player.calculate_temperature(ambient_temperature, equipped_clothing, is_near_fire)
        if effective_temp < 0:
            player.take_damage(5)  # Obrażenia za wychłodzenie
        player.restore_stamina(10)  # --- Regeneracja staminy przy ognisku ---

    # Wynik końcowy
    if player.stats['health'] > 0:
        print("Gracz przetrwał w zimowych warunkach.")
    else:
        print("Gracz zginął z powodu zimna.")
# Listy łupów dla różnych obszarów - eksploracja (Przykładowe jak będzie inventory to zmieni się)
loot_table_urban_exploration = [
    ("Puszka jedzenia", 50),
    ("Bateria", 30),
    ("Narzędzie", 20),
    ("Ubrania", 40),
    ("Lekarstwa", 25)
]

loot_table_forest_exploration = [
    ("Jagody", 60),
    ("Patyki", 70),
    ("Zioła lecznicze", 30),
    ("Grzyby", 40),
    ("Kamienie", 50)
]

loot_table_hunting_exploration = [
    ("Ślady zwierząt", 50),
    ("Zniszczone sidła", 30),
    ("Kości", 20)
]

# Listy łupów dla różnych obszarów - polowanie
loot_table_urban_hunting = [
    ("Szczur", 50),
    ("Gołąb", 30),
    ("Zepsute mięso", 20)
]

loot_table_forest_hunting = [
    ("Surowe mięso", 50),
    ("Kości", 40),
    ("Skóra", 30),
    ("Rogi", 20),
    ("Tłuszcz", 35)
]

loot_table_hunting_hunting = [
    ("Duże surowe mięso", 50),
    ("Gruba skóra", 40),
    ("Kły", 30),
    ("Trofeum", 20)

