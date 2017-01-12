from .trigsection import Condition, Action
from .mbrfsection import MBAction
from ..coder import Coder


# predefined conditions
class CountdownTimer(Condition):
	_id_ = 1
	_args_ = [
		('Comparison' , Coder.Comparison),
		('Time'       , Coder.Default)
	]
	_extra_args_ = {
		'Comparison' : 'comparison',
		'Time'       : 'amount',
		'AtLeast'    : lambda cond, time: cond.Comparison(AtLeast).Time(time),
		'AtMost'     : lambda cond, time: cond.Comparison(AtMost).Time(time),
		'Exactly'    : lambda cond, time: cond.Comparison(Exactly).Time(time)
	}

class Command(Condition):
	_id_ = 2
	_args_ = [
		('Player'     , Coder.Player),
		('Comparison' , Coder.Comparison),
		('Number'     , Coder.Default),
		('Unit'       , Coder.Unit)
	]
	_extra_args_ = {
		'Player'     : 'player',
		'Comparison' : 'comparison',
		'Number'     : 'amount',
		'Unit'       : 'unitid',
		'PUnit'      :  ('Player', 'Unit'),
		'AtLeast'    : lambda cond, number: cond.Comparison(AtLeast).Number(number),
		'AtMost'     : lambda cond, number: cond.Comparison(AtMost).Number(number),
		'Exactly'    : lambda cond, number: cond.Comparison(Exactly).Number(number)
	}

class Bring(Condition):
	_id_ = 3
	_args_ = [
		('Player'     , Coder.Player),
		('Comparison' , Coder.Comparison),
		('Number'     , Coder.Default),
		('Unit'       , Coder.Unit),
		('Location'   , Coder.Location),
	]
	_extra_args_ = {
		'Player'     : 'player',
		'Comparison' : 'comparison',
		'Number'     : 'amount',
		'Unit'       : 'unitid',
		'Location'   : 'locid',
		'AtLeast'    : lambda cond, number: cond.Comparison(AtLeast).Number(number),
		'AtMost'     : lambda cond, number: cond.Comparison(AtMost).Number(number),
		'Exactly'    : lambda cond, number: cond.Comparison(Exactly).Number(number)
	}

class Accumulate(Condition):
	_id_ = 4
	_args_ = [
		('Player'       , Coder.Player),
		('Comparison'   , Coder.Comparison),
		('Number'       , Coder.Default),
		('ResourceType' , Coder.Resource),
	]
	_extra_args_ = {
		'Player'       : 'player',
		'Comparison'   : 'comparison',
		'Number'       : 'amount',
		'ResourceType' : 'restype',
		'AtLeast'      : lambda cond, number: cond.Comparison(AtLeast).Number(number),
		'AtMost'       : lambda cond, number: cond.Comparison(AtMost).Number(number),
		'Exactly'      : lambda cond, number: cond.Comparison(Exactly).Number(number)
	}


class Kills(Condition):
	_id_ = 5
	_args_ = [
		('Player'     , Coder.Player),
		('Comparison' , Coder.Comparison),
		('Number'     , Coder.Default),
		('Unit'       , Coder.Unit),
	]
	_extra_args_ = {
		'Player'      : 'player',
		'Comparison'  : 'comparison',
		'Number'      : 'amount',
		'Unit'        : 'unitid',
		'AtLeast'     : lambda cond, number: cond.Comparison(AtLeast).Number(number),
		'AtMost'      : lambda cond, number: cond.Comparison(AtMost).Number(number),
		'Exactly'     : lambda cond, number: cond.Comparison(Exactly).Number(number)
	}

	@staticmethod
	def GetConstName():
		return 'Kills'

# Kills must be special
Coder.ScoreMap[1] = Coder.ScoreMap[1][:4] + (Kills,) + Coder.ScoreMap[1][5:]

class CommandMost(Condition):
	_id_ = 6
	_args_ = [('Unit', Coder.Unit)]
	_extra_args_ = {'Unit': 'unitid'}

class CommandMostAt(Condition):
	_id_ = 7
	_args_ = [
		('Unit'     , Coder.Unit),
		('Location' , Coder.Location),
	]
	_extra_args_ = {
		'Unit'     : 'unitid',
		'Location' : 'locid',
	}

class MostKills(Condition):
	_id_ = 8
	_args_ = [('Unit', Coder.Unit)]
	_extra_args_ = {'Unit': 'unitid'}

class HighestScore(Condition):
	_id_ = 9
	_args_ = [('ScoreType', Coder.Score)]
	_extra_args_ = {'ScoreType': 'restype'}

class MostResources(Condition):
	_id_ = 10
	_args_ = [('ResourceType', Coder.Resource)]
	_extra_args_ = {'ResourceType': 'restype'}

class Switch(Condition):
	_id_ = 11
	_args_ = [
		('Switch' , Coder.Switch),
		('State'  , Coder.SwitchState),
	]
	_extra_args_ = {
		'Switch' : 'restype',
		'State'  : 'comparison',
	}

class ElapsedTime(Condition):
	_id_ = 12
	_args_ = [
		('Comparison' , Coder.Comparison),
		('Time'       , Coder.Default),
	]
	_extra_args_ = {
		'Comparison' : 'comparison',
		'Time'       : 'amount',
		'AtLeast'    : lambda cond, time: cond.Comparison(AtLeast).Time(time),
		'AtMost'     : lambda cond, time: cond.Comparison(AtMost).Time(time),
		'Exactly'    : lambda cond, time: cond.Comparison(Exactly).Time(time),
	}

class Briefing(Condition):
	_id_ = 13
	_args_ = []
	_extra_args_ = {}

class Opponents(Condition):
	_id_ = 14
	_args_ = [
		('Player'     , Coder.Player),
		('Comparison' , Coder.Comparison),
		('Number'     , Coder.Default),
	]
	_extra_args_ = {
		'Player'     : 'player',
		'Comparison' : 'comparison',
		'Number'     : 'amount',
		'AtLeast'    : lambda cond, number: cond.Comparison(AtLeast).Number(number),
		'AtMost'     : lambda cond, number: cond.Comparison(AtMost).Number(number),
		'Exactly'    : lambda cond, number: cond.Comparison(Exactly).Number(number),
	}

class Deaths(Condition):
	_id_ = 15
	_args_ = [
		('Player'     , Coder.Player),
		('Comparison' , Coder.Comparison),
		('Number'     , Coder.Default),
		('Unit'       , Coder.Unit),
	]
	_extra_args_ = {
		'Player'     : 'player',
		'Comparison' : 'comparison',
		'Number'     : 'amount',
		'Unit'       : 'unitid',
		'AtLeast'    : lambda cond, number: cond.Comparison(AtLeast).Number(number),
		'AtMost'     : lambda cond, number: cond.Comparison(AtMost).Number(number),
		'Exactly'    : lambda cond, number: cond.Comparison(Exactly).Number(number),
	}

class CommandLeast(Condition):
	_id_ = 16
	_args_ = [('Unit', Coder.Unit)]
	_extra_args_ = {'Unit': 'unitid'}

class CommandLeastAt(Condition):
	_id_ = 17
	_args_ = [
		('Unit'     , Coder.Unit),
		('Location' , Coder.Location),
	]
	_extra_args_ = {
		'Unit'     : 'unitid',
		'Location' : 'locid',
	}

class LeastKills(Condition):
	_id_ = 18
	_args_ = [('Unit', Coder.Unit)]
	_extra_args_ = {'Unit': 'unitid'}

class LowestScore(Condition):
	_id_ = 19
	_args_ = [('ScoreType', Coder.Score)]
	_extra_args_ = {'ScoreType': 'restype'}

class LeastResources(Condition):
	_id_ = 20
	_args_ = [('ResourceType', Coder.Resource)]
	_extra_args_ = {'ResourceType': 'restype'}

class Score(Condition):
	_id_ = 21
	_args_ = [
		('Player'     , Coder.Player),
		('ScoreType'  , Coder.Score),
		('Comparison' , Coder.Comparison),
		('Number'     , Coder.Default),
	]
	_extra_args_ = {
		'Player'     : 'player',
		'ScoreType'  : 'restype',
		'Comparison' : 'comparison',
		'Number'     : 'amount',
		'AtLeast'    : lambda cond, number: cond.Comparison(AtLeast).Number(number),
		'AtMost'     : lambda cond, number: cond.Comparison(AtMost).Number(number),
		'Exactly'    : lambda cond, number: cond.Comparison(Exactly).Number(number),
	}

class Always(Condition):
	_id_ = 22
	_args_ = []
	_extra_args_ = {}

class Never(Condition):
	_id_ = 23
	_args_ = []
	_extra_args_ = {}


# predefined actions
class Victory(Action):
	_id_, _flag_ = 1, 4
	_args_ = []
	_extra_args_ = {}

class Defeat(Action):
	_id_, _flag_ = 2, 4
	_args_ = []
	_extra_args_ = {}

class PreserveTrigger(Action):
	_id_, _flag_ = 3, 4
	_args_ = []
	_extra_args_ = {}

class Wait(Action):
	_id_, _flag_ = 4, 4
	_args_ = [('Time', Coder.Default)]
	_extra_args_ = {'Time': 'time'}

class PauseGame(Action):
	_id_, _flag_ = 5, 4
	_args_ = []
	_extra_args_ = {}

class UnpauseGame(Action):
	_id_, _flag_ = 6, 4
	_args_ = []
	_extra_args_ = {}

class Transmission(Action):
	_id_, _flag_ = 7, 4
	_args_ = [
		('Unit'         , Coder.Unit),
		('Where'        , Coder.Location),
		('WAVName'      , Coder.String),
		('TimeModifier' , Coder.Modifier),
		('Time'         , Coder.Default),
		('Text'         , Coder.String),
		('Flag'         , Coder.Default)
	]
	_extra_args_ = {
		'Unit'         : 'unitid',
		'Where'        : 'locid1',
		'WAVName'      : 'wavid',
		'TimeModifier' : 'amount',
		'Time'         : 'time',
		'Text'         : 'strid',
		'Flag'         : 'flag',
	}

	def __init__(self, *args, AlwaysDisplay = 4):
		if len(args) == len(self._args_) - 1:
			args += (AlwaysDisplay, )
		super().__init__(*args)

class PlayWAV(Action):
	_id_, _flag_ = 8, 4
	_args_ = [('WAVName', Coder.String)]
	_extra_args_ = {'WAVName': 'wavid'}

class DisplayText(Action):
	_id_, _flag_ = 9, 4
	_args_ = [('Text', Coder.String)]
	_extra_args_ = {'Text' : 'strid'}

	def __init__(self, *args, AlwaysDisplay = 4):
		if len(args) == len(self._args_) - 1:
			args += (AlwaysDisplay, )
		super().__init__(*args)

class CenterView(Action):
	_id_, _flag_ = 10, 4
	_args_ = [('Where', Coder.Location)]
	_extra_args_ = {'Where': 'locid1'}

class CreateUnitWithProperties(Action):
	_id_, _flag_ = 11, 28
	_args_ = [
		('Count'      , Coder.Default),
		('Unit'       , Coder.Unit),
		('Where'      , Coder.Location),
		('Player'     , Coder.Player),
		('Properties' , Coder.Property),
	]
	_extra_args_ = {
		'Count'      : 'amount',
		'Unit'       : 'unitid',
		'Where'      : 'locid1',
		'Player'     : 'player1',
		'Properties' : 'player2',
	}

class SetMissionObjectives(Action):
	_id_, _flag_ = 12, 4
	_args_ = [('Text', Coder.String)]
	_extra_args_ = {'Text': 'strid'}

class SetSwitch(Action):
	_id_, _flag_ = 13, 4
	_args_ = [
		('Switch' , Coder.Switch),
		('State'  , Coder.SwitchAction),
	]
	_extra_args_ = {
		'Switch' : 'player2',
		'State'  : 'amount',
	}

class SetCountdownTimer(Action):
	_id_, _flag_ = 14, 4
	_args_ = [
		('TimeModifier' , Coder.Modifier),
		('Time'         , Coder.Default),
	]
	_extra_args_ = {
		'TimeModifier' : 'amount',
		'Time'         : 'time',
	}

class RunAIScript(Action):
	_id_, _flag_ = 15, 4
	_args_ = [('Script', Coder.AIScript)]
	_extra_args_ = {'Script': 'player2'}

class RunAIScriptAt(Action):
	_id_, _flag_ = 16, 4
	_args_ = [
		('Script' , Coder.AIScript),
		('Where'  , Coder.Location),
	]
	_extra_args_ = {
		'Script' : 'player2',
		'Where'  : 'locid1',
	}

class LeaderBoardControl(Action):
	_id_, _flag_ = 17, 20
	_args_ = [
		('Unit'  , Coder.Unit),
		('Label' , Coder.String),
	]
	_extra_args_ = {
		'Unit'  : 'unitid',
		'Label' : 'strid',
	}

class LeaderBoardControlAt(Action):
	_id_, _flag_ = 18, 20
	_args_ = [
		('Unit'     , Coder.Unit),
		('Location' , Coder.Location),
		('Label'    , Coder.String),
	]
	_extra_args_ = {
		'Unit'     : 'unitid',
		'Location' : 'locid1',
		'Label'    : 'strid',
	}

class LeaderBoardResources(Action):
	_id_, _flag_ = 19, 4
	_args_ = [
		('ResourceType' , Coder.Resource),
		('Label'        , Coder.String),
	]
	_extra_args_ = {
		'ResourceType' : 'unitid',
		'Label'        : 'strid',
	}

class LeaderBoardKills(Action):
	_id_, _flag_ = 20, 20
	_args_ = [
		('Unit'  , Coder.Unit),
		('Label' , Coder.String),
	]
	_extra_args_ = {
		'Unit'  : 'unitid',
		'Label' : 'strid',
	}

class LeaderBoardScore(Action):
	_id_, _flag_ = 21, 4
	_args_ = [
		('Score' , Coder.Score),
		('Label' , Coder.String),
	]
	_extra_args_ = {
		'Score' : 'unitid',
		'Label' : 'strid',
	}

class KillUnit(Action):
	_id_, _flag_ = 22, 20
	_args_ = [
		('Unit'   , Coder.Unit),
		('Player' , Coder.Player),
	]
	_extra_args_ = {
		'Unit'   : 'unitid',
		'Player' : 'player1',
	}

class KillUnitAt(Action):
	_id_, _flag_ = 23, 20
	_args_ = [
		('Count'     , Coder.Count),
		('Unit'      , Coder.Unit),
		('Where'     , Coder.Location),
		('ForPlayer' , Coder.Player),
	]
	_extra_args_ = {
		'Count'     : 'amount',
		'Unit'      : 'unitid',
		'Where'     : 'locid1',
		'ForPlayer' : 'player1',
	}

class RemoveUnit(Action):
	_id_, _flag_ = 24, 20
	_args_ = [
		('Unit'   , Coder.Unit),
		('Player' , Coder.Player),
	]
	_extra_args_ = {
		'Unit'   : 'unitid',
		'Player' : 'player1',
	}

class RemoveUnitAt(Action):
	_id_, _flag_ = 25, 20
	_args_ = [
		('Count'     , Coder.Count),
		('Unit'      , Coder.Unit),
		('Where'     , Coder.Location),
		('ForPlayer' , Coder.Player),
	]
	_extra_args_ = {
		'Count'     : 'amount',
		'Unit'      : 'unitid',
		'Where'     : 'locid1',
		'ForPlayer' : 'player1',
	}

class SetResources(Action):
	_id_, _flag_ = 26, 4
	_args_ = [
		('Player'       , Coder.Player),
		('Modifier'     , Coder.Modifier),
		('Amount'       , Coder.Default),
		('ResourceType' , Coder.Resource),
	]
	_extra_args_ = {
		'Player'       : 'player1',
		'Modifier'     : 'amount',
		'Amount'       : 'player2',
		'ResourceType' : 'unitid',
	}

class SetScore(Action):
	_id_, _flag_ = 27, 4
	_args_ = [
		('Player'    , Coder.Player),
		('Modifier'  , Coder.Modifier),
		('Amount'    , Coder.Default),
		('ScoreType' , Coder.Score),
	]
	_extra_args_ = {
		'Player'    : 'player1',
		'Modifier'  : 'amount',
		'Amount'    : 'player2',
		'ScoreType' : 'unitid',
	}

class MinimapPing(Action):
	_id_, _flag_ = 28, 4
	_args_ = [('Where', Coder.Location)]
	_extra_args_ = {'Where': 'locid1'}

class TalkingPortrait(Action):
	_id_, _flag_ = 29, 20
	_args_ = [
		('Unit' , Coder.Unit),
		('Time' , Coder.Default),
	]
	_extra_args_ = {
		'Unit' : 'unitid',
		'Time' : 'time',
	}

class MuteUnitSpeech(Action):
	_id_, _flag_ = 30, 4
	_args_ = []
	_extra_args_ = {}

class UnMuteUnitSpeech(Action):
	_id_, _flag_ = 31, 4
	_args_ = []
	_extra_args_ = {}

class LeaderBoardComputerPlayers(Action):
	_id_, _flag_ = 32, 4
	_args_ = [('State', Coder.PropState)]
	_extra_args_ = {'State': 'amount'}

class LeaderBoardGoalControl(Action):
	_id_, _flag_ = 33, 20
	_args_ = [
		('Goal'  , Coder.Default),
		('Unit'  , Coder.Unit),
		('Label' , Coder.String),
	]
	_extra_args_ = {
		'Goal'  : 'player2',
		'Unit'  : 'unitid',
		'Label' : 'strid',
	}

class LeaderBoardGoalControlAt(Action):
	_id_, _flag_ = 34, 20
	_args_ = [
		('Goal'     , Coder.Default),
		('Unit'     , Coder.Unit),
		('Location' , Coder.Location),
		('Label'    , Coder.String),
	]
	_extra_args_ = {
		'Goal'     : 'player2',
		'Unit'     : 'unitid',
		'Location' : 'locid1',
		'Label'    : 'strid',
	}

class LeaderBoardGoalResources(Action):
	_id_, _flag_ = 35, 4
	_args_ = [
		('Goal'         , Coder.Default),
		('ResourceType' , Coder.Resource),
		('Label'        , Coder.String),
	]
	_extra_args_ = {
		'Goal'         : 'player2',
		'ResourceType' : 'unitid',
		'Label'        : 'strid',
	}

class LeaderBoardGoalKills(Action):
	_id_, _flag_ = 36, 20
	_args_ = [
		('Goal'  , Coder.Default),
		('Unit'  , Coder.Unit),
		('Label' , Coder.String),
	]
	_extra_args_ = {
		'Goal'  : 'player2',
		'Unit'  : 'unitid',
		'Label' : 'strid',
	}

class LeaderBoardGoalScore(Action):
	_id_, _flag_ = 37, 4
	_args_ = [
		('Goal'      , Coder.Default),
		('ScoreType' , Coder.Score),
		('Label'     , Coder.String),
	]
	_extra_args_ = {
		'Goal'      : 'player2',
		'ScoreType' : 'unitid',
		'Label'     : 'strid',
	}

class MoveLocation(Action):
	_id_, _flag_ = 38, 20
	_args_ = [
		('Location'     , Coder.Location),
		('OnUnit'       , Coder.Unit),
		('Owner'        , Coder.Player),
		('DestLocation' , Coder.Location),
	]
	_extra_args_ = {
		'Location'     : 'player2',
		'OnUnit'       : 'unitid',
		'Owner'        : 'player1',
		'DestLocation' : 'locid1',
	}

class MoveUnit(Action):
	_id_, _flag_ = 39, 20
	_args_ = [
		('Count'         , Coder.Count),
		('UnitType'      , Coder.Unit),
		('Owner'         , Coder.Player),
		('StartLocation' , Coder.Location),
		('DestLocation'  , Coder.Location),
	]
	_extra_args_ = {
		'Count'         : 'amount',
		'UnitType'      : 'unitid',
		'Owner'         : 'player1',
		'StartLocation' : 'locid1',
		'DestLocation'  : 'player2',
	}

class LeaderBoardGreed(Action):
	_id_, _flag_ = 40, 4
	_args_ = [('Goal', Coder.Default)]
	_extra_args_ = {'Goal': 'player2'}

class SetNextScenario(Action):
	_id_, _flag_ = 41, 4
	_args_ = [('ScenarioName', Coder.String)]
	_extra_args_ = {'ScenarioName': 'strid'}

class SetDoodadState(Action):
	_id_, _flag_ = 42, 20
	_args_ = [
		('State' , Coder.PropState),
		('Unit'  , Coder.Unit),
		('Owner' , Coder.Player),
		('Where' , Coder.Location),
	]
	_extra_args_ = {
		'State' : 'amount',
		'Unit'  : 'unitid',
		'Owner' : 'player1',
		'Where' : 'locid1',
	}

class SetInvincibility(Action):
	_id_, _flag_ = 43, 20
	_args_ = [
		('State' , Coder.PropState),
		('Unit'  , Coder.Unit),
		('Owner' , Coder.Player),
		('Where' , Coder.Location),
	]
	_extra_args_ = {
		'State' : 'amount',
		'Unit'  : 'unitid',
		'Owner' : 'player1',
		'Where' : 'locid1',
	}

class CreateUnit(Action):
	_id_, _flag_ = 44, 20
	_args_ = [
		('Number'    , Coder.Default),
		('Unit'      , Coder.Unit),
		('Where'     , Coder.Location),
		('ForPlayer' , Coder.Player),
	]
	_extra_args_ = {
		'Number'    : 'amount',
		'Unit'      : 'unitid',
		'Where'     : 'locid1',
		'ForPlayer' : 'player1',
	}

class SetDeaths(Action):
	_id_, _flag_ = 45, 20
	_args_ = [
		('Player'   , Coder.Player),
		('Modifier' , Coder.Modifier),
		('Number'   , Coder.Default),
		('Unit'     , Coder.Unit),
	]
	_extra_args_ = {
		'Player'   : 'player1',
		'Modifier' : 'amount',
		'Number'   : 'player2',
		'Unit'     : 'unitid',
	}

class Order(Action):
	_id_, _flag_ = 46, 20
	_args_ = [
		('Unit'          , Coder.Unit),
		('Owner'         , Coder.Player),
		('StartLocation' , Coder.Location),
		('OrderType'     , Coder.Order),
		('DestLocation'  , Coder.Location),
	]
	_extra_args_ = {
		'Unit'          : 'unitid',
		'Owner'         : 'player1',
		'StartLocation' : 'locid1',
		'OrderType'     : 'amount',
		'DestLocation'  : 'player2',
	}

class Comment(Action):
	_id_, _flag_ = 47, 4
	_args_ = [('Text', Coder.String)]
	_extra_args_ = {'Text': 'strid'}

class GiveUnits(Action):
	_id_, _flag_ = 48, 20
	_args_ = [
		('Count'    , Coder.Count),
		('Unit'     , Coder.Unit),
		('Owner'    , Coder.Player),
		('Where'    , Coder.Location),
		('NewOwner' , Coder.Player),
	]
	_extra_args_ = {
		'Count'    : 'amount',
		'Unit'     : 'unitid',
		'Owner'    : 'player1',
		'Where'    : 'locid1',
		'NewOwner' : 'player2',
	}

class ModifyUnitHitPoints(Action):
	_id_, _flag_ = 49, 20
	_args_ = [
		('Count'   , Coder.Count),
		('Unit'    , Coder.Unit),
		('Owner'   , Coder.Player),
		('Where'   , Coder.Location),
		('Percent' , Coder.Default),
	]
	_extra_args_ = {
		'Count'   : 'amount',
		'Unit'    : 'unitid',
		'Owner'   : 'player1',
		'Where'   : 'locid1',
		'Percent' : 'player2',
	}

class ModifyUnitEnergy(Action):
	_id_, _flag_ = 50, 20
	_args_ = [
		('Count'   , Coder.Count),
		('Unit'    , Coder.Unit),
		('Owner'   , Coder.Player),
		('Where'   , Coder.Location),
		('Percent' , Coder.Default),
	]
	_extra_args_ = {
		'Count'   : 'amount',
		'Unit'    : 'unitid',
		'Owner'   : 'player1',
		'Where'   : 'locid1',
		'Percent' : 'player2',
	}

class ModifyUnitShields(Action):
	_id_, _flag_ = 51, 20
	_args_ = [
		('Count'   , Coder.Count),
		('Unit'    , Coder.Unit),
		('Owner'   , Coder.Player),
		('Where'   , Coder.Location),
		('Percent' , Coder.Default),
	]
	_extra_args_ = {
		'Count'   : 'amount',
		'Unit'    : 'unitid',
		'Owner'   : 'player1',
		'Where'   : 'locid1',
		'Percent' : 'player2',
	}

class ModifyUnitResourceAmount(Action):
	_id_, _flag_ = 52, 4
	_args_ = [
		('Count'    , Coder.Count),
		('Owner'    , Coder.Player),
		('Where'    , Coder.Location),
		('NewValue' , Coder.Default),
	]
	_extra_args_ = {
		'Count'    : 'amount',
		'Owner'    : 'player1',
		'Where'    : 'locid1',
		'NewValue' : 'player2',
	}

class ModifyUnitHangarCount(Action):
	_id_, _flag_ = 53, 20
	_args_ = [
		('Add'   , Coder.Default),
		('Count' , Coder.Count),
		('Unit'  , Coder.Unit),
		('Owner' , Coder.Player),
		('Where' , Coder.Location),
	]
	_extra_args_ = {
		'Add'   : 'player2',
		'Count' : 'amount',
		'Unit'  : 'unitid',
		'Owner' : 'player1',
		'Where' : 'locid1',
	}

class PauseTimer(Action):
	_id_, _flag_ = 54, 4
	_args_ = []
	_extra_args_ = {}

class UnpauseTimer(Action):
	_id_, _flag_ = 55, 4
	_args_ = []
	_extra_args_ = {}

class Draw(Action):
	_id_, _flag_ = 56, 4
	_args_ = []
	_extra_args_ = {}

class SetAllianceStatus(Action):
	_id_, _flag_ = 57, 4
	_args_ = [
		('Player' , Coder.Player),
		('Status' , Coder.AllyStatus),
	]
	_extra_args_ = {
		'Player' : 'player1',
		'Status' : 'unitid',
	}

# predefined mbactions
'''
Mission Briefing Actions

                         +0x00   +0x04   +0x08   +0x0C   +0x10   +0x14   +0x18   +0x1A   +0x1B   +0x1C
                                  WORD    WORD   DWORD    BYTE   DWORD    WORD    BYTE    BYTE    BYTE
                                  strid  wavid    time    slot   vtime  unitid acttype     mod    flag
Wait                                              Time                               1
PlayWAV                                    Wav                                       2
TextMessage                       Text            Time                               3
MissionObjective                  Text                                               4
ShowPortrait                                              Slot            Unit       5
HidePortrait                                              Slot                       6
DisplaySpeakingPortrait                           Time    Slot                       7
Transmission                      Text     Wav   WTime    Slot   VTime               8 modifier
'''

class MBWait(MBAction):
	_id_ = 1
	_args_ = [('Time', Coder.Default)]
	_extra_args_ = {'Time' : 'time'}

class MBPlayWAV(MBAction):
	_id_ = 2
	_args_ = [('WAVName', Coder.String)]
	_extra_args_ = {'WAVName' : 'wavid'}

class MBTextMessage(MBAction):
	_id_ = 3
	_args_ = [
		('Text', Coder.String),
		('Time', Coder.Default),
	]
	_extra_args_ = {'Text' : 'strid', 'Time' : 'time'}

class MBMissionObjective(MBAction):
	_id_ = 4
	_args_ = [('Text', Coder.Default)]
	_extra_args_ = {'Text' : 'strid'}

class MBShowPortrait(MBAction):
	_id_ = 5
	_args_ = [
		('Unit', Coder.Unit),
		('Slot', Coder.Default),
	]
	_extra_args_ = {'Unit' : 'unitid', 'Slot' : 'slot'}

class MBHidePortrait(MBAction):
	_id_ = 6
	_args_ = [('Slot', Coder.Default)]
	_extra_args_ = {'Slot' : 'slot'}

class MBDisplaySpeakingPortrait(MBAction):
	_id_ = 7
	_args_ = [
		('Slot', Coder.Default),
		('Time', Coder.Default),
	]
	_extra_args_ = {'Slot' : 'slot', 'Time' : 'time'}

class MBTransmission(MBAction):
	'''
	It may PlayWAV and TextMessage for WAVTIME (MODIFIER) VARTIME miliseconds.
	ex) WavTime = 3, Modifier = Add, VarTime = 5 ==> play for 3 + 5 = 8 seconds
	ex) WavTime = 6, Modifier = SetTo, VarTime = 1 ==> play for 1 second
	'''
	_id_ = 8
	_args_ = [
		('Text', Coder.String),
		('Slot', Coder.Default),
		('VarTime', Coder.Default),
		('Modifier', Coder.Modifier),
		('WAVName', Coder.String),
		('WAVTime', Coder.Default),
	]
	_extra_args_ = {
		'Text'     : 'strid',
		'Slot'     : 'slot',
		'VarTime'  : 'vtime',
		'Modifier' : 'mod',
		'WAVName'  : 'wavid',
		'WAVTime'  : 'time',
	}
