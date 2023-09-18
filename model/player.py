from dataclasses import dataclass


@dataclass
class Player:
    steamID: str
    playerName: str
    kills: int
    deaths: int
    kdr: float
    kpr: float
    awpKills: int
    awpKpr: float
    adr: float
    aud: float
    kast: float
    roundsPlayed: int
    multiKills: int
    tradedKills: int
    tradedDeaths: int
    firstKills: int
    firstDeaths: int
    openingRatio: float
    clutches: int
    clutchesRatio: float
    successFlashes: int
    flashAssists: int
    flashTime: float
    flashTimeMean: float
    headshotPerc: float
    rating: float
    assists: int
    gamesPlayed: int

    @staticmethod
    def from_dict(obj: dict) -> 'Player':
        steamID = str(obj.get("steamID"))
        playerName = str(obj.get("playerName"))
        kills = int(obj.get("kills"))
        deaths = int(obj.get("deaths"))
        kdr = float(obj.get("kdr"))
        kpr = float(obj.get("kpr"))
        awpKills = int(obj.get("awpKills"))
        awpKpr = float(obj.get("awpKpr"))
        adr = float(obj.get("adr"))
        aud = float(obj.get("aud"))
        kast = float(obj.get("kast"))
        roundsPlayed = int(obj.get("roundsPlayed"))
        multiKills = int(obj.get("multiKills"))
        tradedKills = int(obj.get("tradedKills"))
        tradedDeaths = int(obj.get("tradedDeaths"))
        firstKills = int(obj.get("firstKills"))
        firstDeaths = int(obj.get("firstDeaths"))
        openingRatio = float(obj.get("openingRatio"))
        clutches = int(obj.get("clutches"))
        clutchesRatio = float(obj.get("clutchesRatio"))
        successFlashes = int(obj.get("successFlashes"))
        flashAssists = int(obj.get("flashAssists"))
        flashTime = float(obj.get("flashTime"))
        flashTimeMean = float(obj.get("flashTimeMean"))
        headshotPerc = float(obj.get("headshotPerc"))
        rating = float(obj.get("rating"))
        assists = int(obj.get("assists"))
        gamesPlayed = int(obj.get("gamesPlayed"))
        return Player(steamID, playerName, kills, deaths, kdr, kpr, awpKills, awpKpr, adr, aud, kast, roundsPlayed,
                      multiKills, tradedKills, tradedDeaths, firstKills, firstDeaths, openingRatio, clutches,
                      clutchesRatio, successFlashes, flashAssists, flashTime, flashTimeMean, headshotPerc, rating,
                      assists, gamesPlayed)

    def to_dict(self) -> dict:
        result: dict = {"steamID": self.steamID, "playerName": self.playerName, "kills": self.kills,
                        "deaths": self.deaths, "kdr": self.kdr, "kpr": self.kpr, "awpKills": self.awpKills,
                        "awpKpr": self.awpKpr, "adr": self.adr, "aud": self.aud, "kast": self.kast,
                        "roundsPlayed": self.roundsPlayed, "multiKills": self.multiKills,
                        "tradedKills": self.tradedKills, "tradedDeaths": self.tradedDeaths,
                        "firstKills": self.firstKills, "firstDeaths": self.firstDeaths,
                        "openingRatio": self.openingRatio, "clutches": self.clutches,
                        "clutchesRatio": self.clutchesRatio, "successFlashes": self.successFlashes,
                        "flashAssists": self.flashAssists, "flashTime": self.flashTime,
                        "flashTimeMean": self.flashTimeMean, "headshotPerc": self.headshotPerc, "rating": self.rating,
                        "assists": self.assists, "gamesPlayed": self.gamesPlayed}
        return result
