def main():
    import sys

    sys.path.insert(0, "")

    from src.domain.info import Info, InfoRepository
<<<<<<< HEAD
    from src.domain.activity import Activity, ActivityRepository
    from src.domain.wordbyword import WordbywordRepository, Wordbyword
=======
    from src.domain.activities import Activity, ActivityRepository
    from src.domain.wordbyword import Wordbyword, WordbywordRepository
>>>>>>> f9156edee05fd0bd82d969e5bea459053424b735

    database_path = "data/database.db"

    info_repository = InfoRepository(database_path)
    info_repository.save(Info(app_name="irla-kurri"))

<<<<<<< HEAD
    ## Activities

    # Activity1 = Activity(id="1", name="wordbyword")

    # activity_repository = ActivityRepository(database_path)
    # activity_repository.save(Activity1)

    # wordbyword

    Textoriginal = Wordbyword(
        text = "A cien cañones por banda, viento en popa a toda vela"
    )

    wordbyword_repository = WordbywordRepository(database_path)
    wordbyword_repository.save(Textoriginal)

=======
    #Wordbyword
    textoriginal1 = Wordbyword (text = "En un lugar la Mancha de cuyo nombre no quiero acordarme ")
    textoriginal2 = Wordbyword (text = "I can't believe the news today, y close my eyes it make it away ")
    textoriginal3 = Wordbyword (text = "Hala bazan ala ez bazan, sar dadila kalabazan eta atera dadila Foruko plazan ")
    
    wordbyword_repository = WordbywordRepository(database_path)
    
    wordbyword_repository.save(textoriginal1)
    wordbyword_repository.save(textoriginal2)
    wordbyword_repository.save(textoriginal3)
    
    #Activity
    Activity1 = Activity (id = "activity-1", name = "wordbyword" )
                           
    activity_repository = ActivityRepository(database_path)
    activity_repository.save(Activity1)
    
>>>>>>> f9156edee05fd0bd82d969e5bea459053424b735
    print("Base de datos inicializada en" + database_path)


main()
