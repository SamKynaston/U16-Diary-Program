import time

DiaryEntries = []

class Entry():
    def __init__(self, Title, Description):
        self.Title = Title
        self.Description = Description
        self.Date = time.gmtime(0)
        self.Time = time.gmtime(0)
    
    def Edit(self):
        while True:
            print("""
                Diary

                1. Edit Title
                2. Edit Description
                3. Exit

            """)

            Choice = str(input("> "))

            if Choice == "1":
                while True: 
                    Title = str(input("Title: "))

                    if len(Desc) > 0:
                        self.Title = Title
                        break

            elif Choice == "2":
                while True: 
                    Desc = str(input("What's On Your Mind?\n"))

                    if len(Desc) > 0:
                        self.Description = self.Description + "\n\n" + Desc
                        break

            elif Choice == "3":
                break

def NewEntry():
    Title = ""
    Desc  = ""

    while True:
        Title = str(input("Title: "))
    
        if len(Title) > 0:
            break

    while True: 
        Desc = str(input("What's On Your Mind?\n"))

        if len(Desc) > 0:
            break

    DiaryEntries.append(Entry(Title, Desc))

def Search():
  if len(DiaryEntries) > 0:
    while True:
      for i in range(len(DiaryEntries)):
        print(DiaryEntries[i].Title)

      SearchCriteria = str(input("Search: "))
    
      if len(SearchCriteria) > 0:
        for Entry in DiaryEntries:
            if Entry.Title == SearchCriteria:
                print(Entry.Title)
                print(Entry.Description)
                return Entry
      else:
        print("Nothing Found!")
  else:
    print("Nothing to See!")

def Run():
  while True:
    print("""
      Diary

      1. Diary Entry
      2. Search Diaries
      3. Exit

    """)

    choice = str(input("> "))
    
    if choice == "1":
      NewEntry()
    elif choice == "2":
      Search()
    elif choice == "3":
      break

while True:
    Run()
    break