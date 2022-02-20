class Flight:

    def __init__(self, number: str, aircraft):
        '''instance initializer'''
        
        if not number[:2].isalpha():
            raise ValueError(f"No airline code in {number}")
        
        if not number[:2].isupper():
            raise ValueError(f"Invalid airline code {number}")

        if not number[2:].isdigit() and int(number[2:] <= 9999):
            raise ValueError(f"Invalid route number {number}")

        self._number = number
        self._aircraft = aircraft
        rows, seats = self._aircraft.seating_plan()
        
        # list of dictionaries, first element of the list is empty
        # for each rows one dictionary with the seats initialiaed as empty
        self._seating = [None] + [{letter: None for letter in seats} for _ in rows]

    def aircraft_model(self):
        return self._aircraft.model()

    def airline(self):
        return self._number[:2]


    def number(self):
        return self._number



class Aircraft:
    '''
    num_rows 4
    num_seats_per_row 3

    1  A B C 
    2  A B C 
    3  A B C
    4  A B C
    
    '''
    def __init__(self, registration, model, num_rows, num_seats_per_row):
        self._registration = registration
        self._model = model
        self._num_rows = num_rows
        self._num_seats_per_row = num_seats_per_row

    def registration(self):
        return self._registration

        
    def model(self):
        return self._model

    def seating_plan(self):
        return (range(1, self._num_rows + 1), "ABCDEFGHJK"[:self._num_seats_per_row])