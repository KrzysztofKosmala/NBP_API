class UI:

    def selecyCurrencyCodes(codes):
        selected_codes = []
        print("Wybierz dwa kody walutowe z poniższej listy:")
        for i, code in enumerate(codes):
            print(f"{i + 1}. {code}")

        while len(selected_codes) < 2:
            try:
                choice = int(input("Podaj numer wybranego kodu walutowego: "))
                if choice < 1 or choice > len(codes):
                    print("Nieprawidłowy numer. Wybierz ponownie.")
                else:
                    selected_code = codes[choice - 1]
                    if selected_code in selected_codes:
                        print("Ten kod walutowy został już wybrany. Wybierz inny.")
                    else:
                        selected_codes.append(selected_code)
                        print(f"Wybrano kod walutowy: {selected_code}")
            except ValueError:
                print("Nieprawidłowy numer. Wybierz ponownie.")

        return selected_codes