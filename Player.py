class Player:
    def __init__(self, stats):
        self.stats = stats  # Słownik ze statystykami gracza (np. zdrowie, ochrona itp.)

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
        'Zdrowie': 100,
        'max_health': 100,
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

    # Gracz ogrzewa się przy ognisku
    print("Gracz zbliża się do ogniska...")
    is_near_fire = True
    for _ in range(5):
        effective_temp = player.calculate_temperature(ambient_temperature, equipped_clothing, is_near_fire)
        if effective_temp < 0:
            player.take_damage(5)  # Obrażenia za wychłodzenie

    # Wynik końcowy
    if player.stats['Zdrowie'] > 0:
        print("Gracz przetrwał w zimowych warunkach.")
    else:
        print("Gracz zginął z powodu zimna.")
