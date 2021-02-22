# Laboratorio di Programmazione - Esame del 24/02/21

import re  # modulo per le RegEx

data_pattern = '^\d+(\.\d+)?$'
# pattern che rappresenta i valori di time stamp e temperatura
# verrà utilizzato per riconoscere le righe del file
# che contengono i dati formattati nel modo corretto


class ExamException(Exception):
    pass


class CSVTimeSeriesFile:

    def __init__(self, name):
        self.name = name

    def get_data(self):

        if not isinstance(self.name, str):
            raise ExamException('ERRORE, il nome del file deve essere di tipo "string"')
        # controllo se il nome del file inserito è una stringa

        try:
            file = open(self.name, 'r')

        except Exception:
            raise ExamException('ERRORE, il file è inesistente o non leggibile')
        # se il programma fallisce nell'apertura del file viene alzata un'eccezione

        total_file_lines = file.readlines()
        if len(total_file_lines) == 0:
            raise ExamException('ERRORE, il file è vuoto')
        # controllo se il file preso in considerazione è vuoto

        file = open(self.name, 'r')
        total_time_series = []

        for line in file:

            measurement = line.split(',')
            if len(measurement) >= 2:
                measurement = measurement[:2]
                # prendo in considerazione solo i primi due 'campi'

                if re.match(data_pattern, measurement[0]) and re.match(data_pattern, measurement[1]):
                    measurement[0] = round(float(measurement[0]))
                    # se il timestamp non è un numero intero viene arrotondato

                    measurement[1] = float(measurement[1])
                    total_time_series.append(measurement)

        for i in range(len(total_time_series) - 1):
            if total_time_series[i + 1][0] <= total_time_series[i][0]:
                raise ExamException("ERRORE, la serie temporale non è ordinata correttamente")
        # controllo se nella serie ci sono valore fuori ordine o duplicati

        if len(total_time_series) <= 2:
            raise ExamException('ERRORE, quantità di dati insufficiente')
        # controllo se la serie di dati completa ha più di 2 valori
        # dato che sono necessari minimo 3 valori
        # per ciò che ci sia almeno un'inversione di trend

        return total_time_series


def hourly_trend_changes(time_series_list):
    temperature_trend_inversions = []
    hourly_temps_list = []
    # lista con tutti i dati organizzati per ora in cui sono stati registrati

    temporary_temps_list = []
    # i dati di una singola ora vengono memorizzati temporaneamente in questa lista
    # per poi essere inseriti nella lista generale (hourly_temps_list)

    for i in range(len(time_series_list) - 1):
        temporary_temps_list.append(time_series_list[i][1])

        if int(time_series_list[i][0] / 3600) != int(time_series_list[i + 1][0] / 3600):
            hourly_temps_list.append(temporary_temps_list)
            temporary_temps_list = []

    temporary_temps_list.append(time_series_list[-1][1])
    hourly_temps_list.append(temporary_temps_list)
    # inserimento dell'ultimo set (ultima ora) di dati nella lista

    for i in range(len(hourly_temps_list)):
        check_list = []  # lista con i valori necessari per il calcolo delle inversioni
        counter = 0
        trend_checker_list = []
        # lista ausiliaria che verrà utilizzata per il conteggio delle inversioni

        if i > 0:
            check_list.append(hourly_temps_list[i - 1][-1])
        # inserimento dell'ultimo valore dell'ora precedente

        for j in hourly_temps_list[i]:
            check_list.append(j)
        # inserimento di tutti i valori dell'ora attuale

        for k in range(1, len(check_list)):
            if check_list[k] < check_list[k - 1]:
                trend_checker_list.append(0)
                # se il trend è negativo (temperatura diminuisce) il valore è 0

            if check_list[k] > check_list[k - 1]:
                trend_checker_list.append(1)
                # se il trend è positivo (temperatura aumenta) il valore è 1
        # (i casi in cui la temperatura rimane costante nel tempo vengono ignorati)

        for h in range(len(trend_checker_list) - 1):
            if trend_checker_list[h] != trend_checker_list[h + 1]:
                counter += 1
                # conteggio delle inversioni di trend

        temperature_trend_inversions.append(counter)

    return temperature_trend_inversions


time_series_file = CSVTimeSeriesFile('data.csv')
time_series = time_series_file.get_data()
hourly_temps = hourly_trend_changes(time_series)
print(time_series, '\n')
print(hourly_temps, '\n', len(hourly_temps))
