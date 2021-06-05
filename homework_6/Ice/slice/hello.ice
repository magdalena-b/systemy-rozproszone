
#ifndef Hello_ICE
#define Hello_ICE

module Hello {

    exception SongNotFoundError {};
    exception WrongTimeError {};

    interface IRecommendMusic {
        string recommendMusic();
    };

    interface ISetTimer {
        void setTimer(string time) throws WrongTimeError;
    };

    interface IGetAPI {
        string getPandaFact();
        string getKoalaFact();
        string getLyrics(string title, string artist) throws SongNotFoundError;
    };

    interface IGetRandomNumer {
        int getRandomInt();
        double getRandomDouble();
    };


};

#endif
