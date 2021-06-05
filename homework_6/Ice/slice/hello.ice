
#ifndef Hello_ICE
#define Hello_ICE

module Hello {

    exception SongNotFoundError {};
    exception WrongNumberError {};

    interface IRecommendMusic {
        string recommendMusic();
    };

    interface ISetTimer {
        string setTimer(string time) throws WrongNumberError;
    };

    interface IGetAPI {
        string getPandaFact();
        string getKoalaFact();
        string getLyrics(string title, string artist) throws SongNotFoundError;
    };

    interface IGetRandomNumber {
        int getRandomInt(string min, string max) throws WrongNumberError;
        double getRandomDouble(string min, string max) throws WrongNumberError;
    };


};

#endif
