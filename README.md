# \# StoreFlow – System zarządzania stanami magazynowymi

# 

# Aplikacja internetowa wspierająca małe sklepy detaliczne w ewidencjonowaniu produktów, kontrolowaniu stanów magazynowych oraz obsłudze przyjęć (PZ) i wydań (WZ) towaru.

# 

# \## Zespół projektowy i role Scrum

# 

# \* \*\*Kacper Dzierwa\*\* – Product Owner \& Developer

# \* \*\*Sebastian Batko\*\* – Scrum Master \& Developer

# \* \*\*Kamil Chmiel\*\* – Developer \& Interesariusz (symulacja roli właściciela sklepu)

# \* \*\*Jakub Osmenda\*\* – Developer \& DevOps

# 

# \## Architektura projektu

# 

# Projekt wykorzystuje architekturę warstwową:

# \* `app/routes/` – warstwa prezentacji (endpointy REST API, walidacja żądań).

# \* `app/services/` – warstwa logiki biznesowej (reguły magazynowe, obsługa PZ/WZ).

# \* `app/models/` – warstwa dostępu do danych (encję i relacje bazodanowe).

# 

# \## Instrukcja uruchomienia lokalnego

# 

# \### Wymagania wstępne

# \* Python 3.11+

# 

# \### Kroki uruchomienia

# 

# 1\. Sklonuj repozytorium i wejdź do katalogu projektu:

# &#x20;  ```bash

# &#x20;  git clone <link-do-repozytorium>

# &#x20;  cd storeflow

