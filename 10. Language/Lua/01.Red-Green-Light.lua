local spinSound = workspace.Sfx.DOLL_SPIN_SOUND
local dollSound = workspace.Sfx.DOLL_SOUND
local dollHead = workspace["Squid Game"].Doll.Head

local isRedLight = false

local RunService = game:GetService("RunService")

local function greenLight()
	isRedLight = false
	spinSound:Play()
	dollHead.CFrame = dollHead.CFrame * CFrame.Angles(0, math.rad(180), 0)  -- 뒤돌아보기
	dollSound:Play()
end

local function redLight()
	isRedLight = true
	spinSound:Play()
	dollHead.CFrame = dollHead.CFrame * CFrame.Angles(0, math.rad(-180), 0) -- 앞을 보기
	wait(5)
	greenLight()
end

local function findPlayers()
	-- 모든 플레이어 가져오기
	local allPlayer = game.Players:GetPlayers()

	for _, player in pairs(allPlayer) do
		if player.Character then
			local humanoid = player.Character:FindFirstChild("Humanoid")
			local isMoving = humanoid.MoveDirection.magnitude == 1
			if isMoving and isRedLight then
				humanoid.Health = 0  -- 대문자 유의
			end
		end
	end
end


wait(5)
greenLight()


RunService.Heartbeat:Connect(findPlayers)  -- 프레임마다 findPlayers 실행

dollSound.Ended:Connect(redLight) -- dollSound 종료시 redRight를 실행하는 eventListner


-- 함수 선언 및 호출 순서가 엄청 중요하다!