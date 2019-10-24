def EmptyLine():
    """
    prints an empty line
    :return: nothing
    """
    print('')

def DisplayAppName():
    """
    displays the name of the app
    :return: nothing
    """
    print("/-----------------------\ ")
    print("| Cheltuieli De Familie | ")
    print("\-----------------------/ ")
    EmptyLine()

def DisplayCommands():
    """
    displays all the posible commands that can be inputed, with a description
    :return: nothing
    """
    print("COMENZI:")
    print("Adaugare si actualizare:\n",
    "     [1]: Adauga o noua cheltuiala;\n",
    "     [2]: Actualizeaza o cheltuiala;\n",
    "Stergere:\n",
    "     #[3]: Sterge toate cheltuielile dintr-o zi;\n",
    "     #[4]: Sterge toate cheltuielile dintr-un interval de zile;\n",
    "     #[5]: Sterge toate cheltuielile de un anumit tip;\n",
    "Cautari:\n",
    "     [6]: Cauta toate cheltuielile mai mari decat o anumita suma;\n",
    "     #[7]: Cauta toate cheltuielile efectuate inainte de o zi anume si mai mici decat o anumita suma;\n",
    "     #[8]: Cauta toate cheltuielile de un anumit tip;\n",
    "Rapoarte:\n",
    "     [9]: Afiseaza suma totala pentru un anumit tip de cheltuieli;\n",
    "    #[10]: Afiseaza ziua cu suma cheltuita maxima;\n",
    "    #[11]: Afiseaza toate cheltuielile ce au o anumta suma;\n",
    "    #[12]: Afiseaza toate cheltuielile sortate dupa tip;\n",
    "Filtrare:\n",
    "    [13]: Elimina toate cheltuielile de un anumit tip;\n",
    "    #[14]: Elimina toate cheltuielile mai mici decat o suma data;\n",
    "Anulare:\n",
    "    #[15]: Anuleaza ultima operatie efectuata asupra cheltuielilor;\n"
    "[16]: Iesire din aplicatie.")
    EmptyLine()

def ShowMenu():
    """
    prints the menu in the console
    :return: nothing
    """
    DisplayAppName()
    DisplayCommands()
    