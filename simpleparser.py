'''
Used on making sections.condact
'''

def ConditionParse(string):
	'''
	def Kills(Player, Comparison, Number, Unit):
	    Player = ParsePlayer(Player)
	    Comparison = ParseComparison(Comparison)
	    Unit = ParseUnit(Unit)
	    return Condition(0, Player, Number, Unit, Comparison, 5, 0, 0)

	SHOULD RETURN

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
			'Unit'        : 'unitid'
		}
	'''
	originalargs = ['locid', 'player', 'amount', 'unitid',
		'comparison', 'condtype', 'restype', 'flag']
	string = string.strip('\n')
	res = []

	for cond in string.split('\n\n\n'):
		s = ''
		cond = cond.strip('\n')
		lines = cond.split('\n')
		
		defline, parsingline, returnline = lines[0], lines[1:-1], lines[-1]
		
		# defline
		i = defline.index('(')
		name = defline[4:i]
		args = defline[i+1:defline.index(')')].split(', ')
		if args[0] == '':
			args = []

		# parsingline
		arg_method_dict = {}
		for line in parsingline:
			p = line.strip().split(' = ')
			arg_method_dict[p[0]] = p[1][5:p[1].index('(')] # 4 from Parse

		# returnline
		retvals = returnline[returnline.index('(')+1:returnline.index(')')].split(', ')
		idval = int(retvals[5])

		s += "class %s(Condition):\n" % name
		s += "\t_id_ = %d\n" % idval
		if len(args) == 0:
			s += "\t_args_ = []\n"
			s += "\t_extra_args_ = {}\n"
		elif len(args) == 1:
			arg = args[0]
			s += "\t_args_ = [('%s', Coder.%s)]\n" % (arg, arg_method_dict.get(arg, 'Default'))
			s += "\t_extra_args_ = {'%s': '%s'}\n" % (arg, originalargs[retvals.index(arg)])
		else:
			argname_maxlen = max(map(len, args))
			s += "\t_args_ = [\n"
			for arg in args:
				s += "\t\t('%s'%s, Coder.%s),\n" \
					% (arg, ' '*(argname_maxlen-len(arg)+1), arg_method_dict.get(arg, 'Default'))
			s += "\t]\n"
			s += "\t_extra_args_ = {\n"
			for arg in args:
				s += "\t\t'%s'%s: '%s',\n" \
					% (arg, ' '*(argname_maxlen-len(arg)+1), originalargs[retvals.index(arg)])
			s += "\t}\n"

		res.append(s)

	return '\n'.join(res)

def ActionParse(string):
	'''
	def MoveLocation(Location, OnUnit, Owner, DestLocation):
	    Location = ParseLocation(Location)
	    OnUnit = ParseUnit(OnUnit)
	    Owner = ParsePlayer(Owner)
	    DestLocation = ParseLocation(DestLocation)
	    return Action(DestLocation, 0, 0, 0, Owner, Location, OnUnit, 38, 0, 20)

	SHOULD RETURN

	class MoveLocation(Action):
		_id_, _flag_ = 38, 20
		_args_ = [
			('Location'     , Coder.Location),
			('OnUnit'       , Coder.Unit),
			('Owner'        , Coder.Player),
			('DestLocation' , Coder.Location),
		]
		_extra_args_ = {
			'Player'      : 'player',
			'Comparison'  : 'comparison',
			'Number'      : 'amount',
			'Unit'        : 'unitid'
		}
	'''
	originalargs = ['locid1', 'strid', 'wavid', 'time', 'player1',
                       'player2', 'unitid', 'acttype', 'amount', 'flags']
	string = string.strip('\n')
	res = []

	for cond in string.split('\n\n\n'):
		s = ''
		cond = cond.strip('\n')
		lines = cond.split('\n')
		
		defline, parsingline, returnline = lines[0], lines[1:-1], lines[-1]
		
		# defline
		i = defline.index('(')
		name = defline[4:i]
		args = defline[i+1:defline.index(')')].split(', ')
		if args[0] == '':
			args = []

		# parsingline
		arg_method_dict = {}
		for line in parsingline:
			p = line.strip().split(' = ')
			arg_method_dict[p[0]] = p[1][5:p[1].index('(')] # 4 from Parse

		# returnline
		retvals = returnline[returnline.index('(')+1:returnline.index(')')].split(', ')
		idval = int(retvals[7])
		flagval = int(retvals[9])

		# test
		for p in (0, 1, 2, 3, 4, 5, 6, 8):
			if retvals[p][0] in '123456789':
				raise RuntimeError()

		s += "class %s(Action):\n" % name
		s += "\t_id_, _flag_ = %d, %d\n" % (idval, flagval)
		if len(args) == 0:
			s += "\t_args_ = []\n"
			s += "\t_extra_args_ = {}\n"
		elif len(args) == 1:
			arg = args[0]
			s += "\t_args_ = [('%s', Coder.%s)]\n" % (arg, arg_method_dict.get(arg, 'Default'))
			s += "\t_extra_args_ = {'%s': '%s'}\n" % (arg, originalargs[retvals.index(arg)])
		else:
			argname_maxlen = max(map(len, args))
			s += "\t_args_ = [\n"
			for arg in args:
				s += "\t\t('%s'%s, Coder.%s),\n" \
					% (arg, ' '*(argname_maxlen-len(arg)+1), arg_method_dict.get(arg, 'Default'))
			s += "\t]\n"
			s += "\t_extra_args_ = {\n"
			for arg in args:
				s += "\t\t'%s'%s: '%s',\n" \
					% (arg, ' '*(argname_maxlen-len(arg)+1), originalargs[retvals.index(arg)])
			s += "\t}\n"

		res.append(s)

	return '\n'.join(res)

conditions = \
'''

def Kills(Player, Comparison, Number, Unit):
    Player = ParsePlayer(Player)
    Comparison = ParseComparison(Comparison)
    Unit = ParseUnit(Unit)
    return Condition(0, Player, Number, Unit, Comparison, 5, 0, 0)


def CommandMost(Unit):
    Unit = ParseUnit(Unit)
    return Condition(0, 0, 0, Unit, 0, 6, 0, 0)


def CommandMostAt(Unit, Location):
    Unit = ParseUnit(Unit)
    Location = ParseLocation(Location)
    return Condition(Location, 0, 0, Unit, 0, 7, 0, 0)


def MostKills(Unit):
    Unit = ParseUnit(Unit)
    return Condition(0, 0, 0, Unit, 0, 8, 0, 0)


def HighestScore(ScoreType):
    ScoreType = ParseScore(ScoreType)
    return Condition(0, 0, 0, 0, 0, 9, ScoreType, 0)


def MostResources(ResourceType):
    ResourceType = ParseResource(ResourceType)
    return Condition(0, 0, 0, 0, 0, 10, ResourceType, 0)


def Switch(Switch, State):
    Switch = ParseSwitch(Switch);
    State = ParseSwitchState(State)
    return Condition(0, 0, 0, 0, State, 11, Switch, 0)


def ElapsedTime(Comparison, Time):
    Comparison = ParseComparison(Comparison)
    return Condition(0, 0, Time, 0, Comparison, 12, 0, 0)


def Briefing():
    return Condition(0, 0, 0, 0, 0, 13, 0, 0)


def Opponents(Player, Comparison, Number):
    Player = ParsePlayer(Player)
    Comparison = ParseComparison(Comparison)
    return Condition(0, Player, Number, 0, Comparison, 14, 0, 0)


def Deaths(Player, Comparison, Number, Unit):
    Player = ParsePlayer(Player)
    Comparison = ParseComparison(Comparison)
    Unit = ParseUnit(Unit)
    return Condition(0, Player, Number, Unit, Comparison, 15, 0, 0)


def CommandLeast(Unit):
    Unit = ParseUnit(Unit)
    return Condition(0, 0, 0, Unit, 0, 16, 0, 0)


def CommandLeastAt(Unit, Location):
    Unit = ParseUnit(Unit)
    Location = ParseLocation(Location)
    return Condition(Location, 0, 0, Unit, 0, 17, 0, 0)


def LeastKills(Unit):
    Unit = ParseUnit(Unit)
    return Condition(0, 0, 0, Unit, 0, 18, 0, 0)


def LowestScore(ScoreType):
    ScoreType = ParseScore(ScoreType)
    return Condition(0, 0, 0, 0, 0, 19, ScoreType, 0)


def LeastResources(ResourceType):
    ResourceType = ParseResource(ResourceType)
    return Condition(0, 0, 0, 0, 0, 20, ResourceType, 0)


def Score(Player, ScoreType, Comparison, Number):
    Player = ParsePlayer(Player)
    ScoreType = ParseScore(ScoreType)
    Comparison = ParseComparison(Comparison)
    return Condition(0, Player, Number, 0, Comparison, 21, ScoreType, 0)


def Always():
    return Condition(0, 0, 0, 0, 0, 22, 0, 0)


def Never():
    return Condition(0, 0, 0, 0, 0, 23, 0, 0)
'''

# Transmission is special
actions = \
'''

def NoAction():
    return Action(0, 0, 0, 0, 0, 0, 0, 0, 0, 4)


def Victory():
    return Action(0, 0, 0, 0, 0, 0, 0, 1, 0, 4)


def Defeat():
    return Action(0, 0, 0, 0, 0, 0, 0, 2, 0, 4)


def PreserveTrigger():
    return Action(0, 0, 0, 0, 0, 0, 0, 3, 0, 4)


def Wait(Time):
    return Action(0, 0, 0, Time, 0, 0, 0, 4, 0, 4)


def PauseGame():
    return Action(0, 0, 0, 0, 0, 0, 0, 5, 0, 4)


def UnpauseGame():
    return Action(0, 0, 0, 0, 0, 0, 0, 6, 0, 4)


def PlayWAV(WAVName):
    WAVName = ParseString(WAVName)
    return Action(0, 0, WAVName, 0, 0, 0, 0, 8, 0, 4)


def CenterView(Where):
    Where = ParseLocation(Where)
    return Action(Where, 0, 0, 0, 0, 0, 0, 10, 0, 4)


def CreateUnitWithProperties(Count, Unit, Where, Player, Properties):
    Unit = ParseUnit(Unit)
    Where = ParseLocation(Where)
    Player = ParsePlayer(Player)
    Properties = ParseProperty(Properties)
    return Action(Where, 0, 0, 0, Player, Properties, Unit, 11, Count, 28)


def SetMissionObjectives(Text):
    Text = ParseString(Text)
    return Action(0, Text, 0, 0, 0, 0, 0, 12, 0, 4)


def SetSwitch(Switch, State):
    Switch = ParseSwitch(Switch)
    State = ParseSwitchAction(State)
    return Action(0, 0, 0, 0, 0, Switch, 0, 13, State, 4)


def SetCountdownTimer(TimeModifier, Time):
    TimeModifier = ParseModifier(TimeModifier)
    return Action(0, 0, 0, Time, 0, 0, 0, 14, TimeModifier, 4)


def RunAIScript(Script):
    Script = ParseAIScript(Script)
    return Action(0, 0, 0, 0, 0, Script, 0, 15, 0, 4)


def RunAIScriptAt(Script, Where):
    Script = ParseAIScript(Script)
    Where = ParseLocation(Where)
    return Action(Where, 0, 0, 0, 0, Script, 0, 16, 0, 4)


def LeaderBoardControl(Unit, Label):
    Unit = ParseUnit(Unit)
    Label = ParseString(Label)
    return Action(0, Label, 0, 0, 0, 0, Unit, 17, 0, 20)


def LeaderBoardControlAt(Unit, Location, Label):
    Unit = ParseUnit(Unit)
    Location = ParseLocation(Location)
    Label = ParseString(Label)
    return Action(Location, Label, 0, 0, 0, 0, Unit, 18, 0, 20)


def LeaderBoardResources(ResourceType, Label):
    ResourceType = ParseResource(ResourceType)
    Label = ParseString(Label)
    return Action(0, Label, 0, 0, 0, 0, ResourceType, 19, 0, 4)


def LeaderBoardKills(Unit, Label):
    Unit = ParseUnit(Unit)
    Label = ParseString(Label)
    return Action(0, Label, 0, 0, 0, 0, Unit, 20, 0, 20)


def LeaderBoardScore(Score, Label):
    Score = ParseScore(Score)
    Label = ParseString(Label)
    return Action(0, Label, 0, 0, 0, 0, Score, 21, 0, 4)


def KillUnit(Unit, Player):
    Unit = ParseUnit(Unit)
    Player = ParsePlayer(Player)
    return Action(0, 0, 0, 0, Player, 0, Unit, 22, 0, 20)


def KillUnitAt(Count, Unit, Where, ForPlayer):
    Count = ParseCount(Count)
    Unit = ParseUnit(Unit)
    Where = ParseLocation(Where)
    ForPlayer = ParsePlayer(ForPlayer)
    return Action(Where, 0, 0, 0, ForPlayer, 0, Unit, 23, Count, 20)


def RemoveUnit(Unit, Player):
    Unit = ParseUnit(Unit)
    Player = ParsePlayer(Player)
    return Action(0, 0, 0, 0, Player, 0, Unit, 24, 0, 20)


def RemoveUnitAt(Count, Unit, Where, ForPlayer):
    Count = ParseCount(Count)
    Unit = ParseUnit(Unit)
    Where = ParseLocation(Where)
    ForPlayer = ParsePlayer(ForPlayer)
    return Action(Where, 0, 0, 0, ForPlayer, 0, Unit, 25, Count, 20)


def SetResources(Player, Modifier, Amount, ResourceType):
    Player = ParsePlayer(Player)
    Modifier = ParseModifier(Modifier)
    ResourceType = ParseResource(ResourceType)
    return Action(0, 0, 0, 0, Player, Amount, ResourceType, 26, Modifier, 4)


def SetScore(Player, Modifier, Amount, ScoreType):
    Player = ParsePlayer(Player)
    Modifier = ParseModifier(Modifier)
    ScoreType = ParseScore(ScoreType)
    return Action(0, 0, 0, 0, Player, Amount, ScoreType, 27, Modifier, 4)


def MinimapPing(Where):
    Where = ParseLocation(Where)
    return Action(Where, 0, 0, 0, 0, 0, 0, 28, 0, 4)


def TalkingPortrait(Unit, Time):
    Unit = ParseUnit(Unit)
    return Action(0, 0, 0, Time, 0, 0, Unit, 29, 0, 20)


def MuteUnitSpeech():
    return Action(0, 0, 0, 0, 0, 0, 0, 30, 0, 4)


def UnMuteUnitSpeech():
    return Action(0, 0, 0, 0, 0, 0, 0, 31, 0, 4)


def LeaderBoardComputerPlayers(State):
    State = ParsePropState(State)
    return Action(0, 0, 0, 0, 0, 0, 0, 32, State, 4)


def LeaderBoardGoalControl(Goal, Unit, Label):
    Unit = ParseUnit(Unit)
    Label = ParseString(Label)
    return Action(0, Label, 0, 0, 0, Goal, Unit, 33, 0, 20)


def LeaderBoardGoalControlAt(Goal, Unit, Location, Label):
    Unit = ParseUnit(Unit)
    Location = ParseLocation(Location)
    Label = ParseString(Label)
    return Action(Location, Label, 0, 0, 0, Goal, Unit, 34, 0, 20)


def LeaderBoardGoalResources(Goal, ResourceType, Label):
    ResourceType = ParseResource(ResourceType)
    Label = ParseString(Label)
    return Action(0, Label, 0, 0, 0, Goal, ResourceType, 35, 0, 4)


def LeaderBoardGoalKills(Goal, Unit, Label):
    Unit = ParseUnit(Unit)
    Label = ParseString(Label)
    return Action(0, Label, 0, 0, 0, Goal, Unit, 36, 0, 20)


def LeaderBoardGoalScore(Goal, ScoreType, Label):
    ScoreType = ParseScore(ScoreType)
    Label = ParseString(Label)
    return Action(0, Label, 0, 0, 0, Goal, ScoreType, 37, 0, 4)


def MoveLocation(Location, OnUnit, Owner, DestLocation):
    Location = ParseLocation(Location)
    OnUnit = ParseUnit(OnUnit)
    Owner = ParsePlayer(Owner)
    DestLocation = ParseLocation(DestLocation)
    return Action(DestLocation, 0, 0, 0, Owner, Location, OnUnit, 38, 0, 20)


def MoveUnit(Count, UnitType, Owner, StartLocation, DestLocation):
    Count = ParseCount(Count)
    UnitType = ParseUnit(UnitType)
    Owner = ParsePlayer(Owner)
    StartLocation = ParseLocation(StartLocation)
    DestLocation = ParseLocation(DestLocation)
    return Action(StartLocation, 0, 0, 0, Owner, DestLocation, UnitType, 39, Count, 20)


def LeaderBoardGreed(Goal):
    return Action(0, 0, 0, 0, 0, Goal, 0, 40, 0, 4)


def SetNextScenario(ScenarioName):
    ScenarioName = ParseString(ScenarioName)
    return Action(0, ScenarioName, 0, 0, 0, 0, 0, 41, 0, 4)


def SetDoodadState(State, Unit, Owner, Where):
    State = ParsePropState(State)
    Unit = ParseUnit(Unit)
    Owner = ParsePlayer(Owner)
    Where = ParseLocation(Where)
    return Action(Where, 0, 0, 0, Owner, 0, Unit, 42, State, 20)


def SetInvincibility(State, Unit, Owner, Where):
    State = ParsePropState(State)
    Unit = ParseUnit(Unit)
    Owner = ParsePlayer(Owner)
    Where = ParseLocation(Where)
    return Action(Where, 0, 0, 0, Owner, 0, Unit, 43, State, 20)


def CreateUnit(Number, Unit, Where, ForPlayer):
    Unit = ParseUnit(Unit)
    Where = ParseLocation(Where)
    ForPlayer = ParsePlayer(ForPlayer)
    return Action(Where, 0, 0, 0, ForPlayer, 0, Unit, 44, Number, 20)


def SetDeaths(Player, Modifier, Number, Unit):
    Player = ParsePlayer(Player)
    Modifier = ParseModifier(Modifier)
    Unit = ParseUnit(Unit)
    return Action(0, 0, 0, 0, Player, Number, Unit, 45, Modifier, 20)


def Order(Unit, Owner, StartLocation, OrderType, DestLocation):
    Unit = ParseUnit(Unit)
    Owner = ParsePlayer(Owner)
    StartLocation = ParseLocation(StartLocation)
    OrderType = ParseOrder(OrderType)
    DestLocation = ParseLocation(DestLocation)
    return Action(StartLocation, 0, 0, 0, Owner, DestLocation, Unit, 46, OrderType, 20)


def Comment(Text):
    Text = ParseString(Text)
    return Action(0, Text, 0, 0, 0, 0, 0, 47, 0, 4)


def GiveUnits(Count, Unit, Owner, Where, NewOwner):
    Count = ParseCount(Count)
    Unit = ParseUnit(Unit)
    Owner = ParsePlayer(Owner)
    Where = ParseLocation(Where)
    NewOwner = ParsePlayer(NewOwner)
    return Action(Where, 0, 0, 0, Owner, NewOwner, Unit, 48, Count, 20)


def ModifyUnitHitPoints(Count, Unit, Owner, Where, Percent):
    Count = ParseCount(Count)
    Unit = ParseUnit(Unit)
    Owner = ParsePlayer(Owner)
    Where = ParseLocation(Where)
    return Action(Where, 0, 0, 0, Owner, Percent, Unit, 49, Count, 20)


def ModifyUnitEnergy(Count, Unit, Owner, Where, Percent):
    Count = ParseCount(Count)
    Unit = ParseUnit(Unit)
    Owner = ParsePlayer(Owner)
    Where = ParseLocation(Where)
    return Action(Where, 0, 0, 0, Owner, Percent, Unit, 50, Count, 20)


def ModifyUnitShields(Count, Unit, Owner, Where, Percent):
    Count = ParseCount(Count)
    Unit = ParseUnit(Unit)
    Owner = ParsePlayer(Owner)
    Where = ParseLocation(Where)
    return Action(Where, 0, 0, 0, Owner, Percent, Unit, 51, Count, 20)


def ModifyUnitResourceAmount(Count, Owner, Where, NewValue):
    Count = ParseCount(Count)
    Owner = ParsePlayer(Owner)
    Where = ParseLocation(Where)
    return Action(Where, 0, 0, 0, Owner, NewValue, 0, 52, Count, 4)


def ModifyUnitHangarCount(Add, Count, Unit, Owner, Where):
    Count = ParseCount(Count)
    Unit = ParseUnit(Unit)
    Owner = ParsePlayer(Owner)
    Where = ParseLocation(Where)
    return Action(Where, 0, 0, 0, Owner, Add, Unit, 53, Count, 20)


def PauseTimer():
    return Action(0, 0, 0, 0, 0, 0, 0, 54, 0, 4)


def UnpauseTimer():
    return Action(0, 0, 0, 0, 0, 0, 0, 55, 0, 4)


def Draw():
    return Action(0, 0, 0, 0, 0, 0, 0, 56, 0, 4)


def SetAllianceStatus(Player, Status):
    Player = ParsePlayer(Player)
    Status = ParseAllyStatus(Status)
    return Action(0, 0, 0, 0, Player, 0, Status, 57, 0, 4)
'''

# print(ConditionParse(conditions))
print(ActionParse(actions))
# exceptional case
'''

def DisplayText(Text, AlwaysDisplay=4):
    Text = ParseString(Text)
    return Action(0, Text, 0, 0, 0, 0, 0, 9, 0, AlwaysDisplay)

def Transmission(Unit, Where, WAVName, TimeModifier, Time, Text, AlwaysDisplay = 4):
    Unit = ParseUnit(Unit)
    Where = ParseLocation(Where)
    WAVName = ParseString(WAVName)
    TimeModifier = ParseModifier(TimeModifier)
    Text = ParseString(Text)
    return Action(Where, Text, WAVName, Time, 0, 0, Unit, 7, TimeModifier, AlwaysDisplay)
'''