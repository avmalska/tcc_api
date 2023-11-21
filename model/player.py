from dataclasses import dataclass
from pydantic import BaseModel


@dataclass
class Player:
    steamID: str
    playerName: str
    kills: float
    deaths: float
    kdr: float
    kpr: float
    awpKills: float
    awpKpr: float
    adr: float
    aud: float
    kast: float
    roundsPlayed: float
    multiKills: float
    tradedKills: float
    tradedDeaths: float
    firstKills: float
    firstDeaths: float
    openingRatio: float
    clutches: float
    clutchesRatio: float
    successFlashes: float
    flashAssists: float
    flashTime: float
    flashTimeMean: float
    headshotPerc: float
    rating: float
    assists: float
    gamesPlayed: float

    @staticmethod
    def from_dict(obj: dict) -> 'Player':
        steamID = str(obj.get("steamID"))
        playerName = str(obj.get("playerName"))
        kills = float(obj.get("kills"))
        deaths = float(obj.get("deaths"))
        kdr = float(obj.get("kdr"))
        kpr = float(obj.get("kpr"))
        awpKills = float(obj.get("awpKills"))
        awpKpr = float(obj.get("awpKpr"))
        adr = float(obj.get("adr"))
        aud = float(obj.get("aud"))
        kast = float(obj.get("kast"))
        roundsPlayed = float(obj.get("roundsPlayed"))
        multiKills = float(obj.get("multiKills"))
        tradedKills = float(obj.get("tradedKills"))
        tradedDeaths = float(obj.get("tradedDeaths"))
        firstKills = float(obj.get("firstKills"))
        firstDeaths = float(obj.get("firstDeaths"))
        openingRatio = float(obj.get("openingRatio"))
        clutches = float(obj.get("clutches"))
        clutchesRatio = float(obj.get("clutchesRatio"))
        successFlashes = float(obj.get("successFlashes"))
        flashAssists = float(obj.get("flashAssists"))
        flashTime = float(obj.get("flashTime"))
        flashTimeMean = float(obj.get("flashTimeMean"))
        headshotPerc = float(obj.get("headshotPerc"))
        rating = float(obj.get("rating"))
        assists = float(obj.get("assists"))
        gamesPlayed = float(obj.get("gamesPlayed"))
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


class NewPlayerIncoming(BaseModel):
    steamID: str
    name: str
    kdr: float
    kpr: float
    awpKpr: float
    adr: float
    aud: float
    kast: float
    multiKills: float
    openingRatio: float
    clutchesRatio: float
    flashTimeMean: float
    rating: float


class NewPlayer:
    steamID: str
    name: str
    kdr: float
    kpr: float
    awpKpr: float
    adr: float
    aud: float
    kast: float
    multiKills: float
    openingRatio: float
    clutchesRatio: float
    flashTimeMean: float
    rating: float

    def to_df_dict(self) -> dict:
        result: dict = {"kdr": [self.kdr], "kpr": [self.kpr], "awpKpr": [self.awpKpr], "adr": [self.adr],
                        "aud": [self.aud], "kast": [self.kast], "multiKills": [self.multiKills],
                        "openingRatio": [self.openingRatio], "clutchesRatio": [self.clutchesRatio],
                        "flashTimeMean": [self.flashTimeMean], "rating": [self.rating]}
        return result

    @staticmethod
    def from_incoming(incoming_player: NewPlayerIncoming):
        new_player = NewPlayer()
        new_player.steamID = incoming_player.steamID
        new_player.name = incoming_player.name
        new_player.kdr = incoming_player.kdr
        new_player.kpr = incoming_player.kpr
        new_player.awpKpr = incoming_player.awpKpr
        new_player.adr = incoming_player.adr
        new_player.aud = incoming_player.aud
        new_player.kast = incoming_player.kast
        new_player.multiKills = incoming_player.multiKills
        new_player.openingRatio = incoming_player.openingRatio
        new_player.clutchesRatio = incoming_player.clutchesRatio
        new_player.flashTimeMean = incoming_player.flashTimeMean
        new_player.rating = incoming_player.rating
        return new_player
