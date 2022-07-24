local players = game:GetService("Players")
local parent = script.Parent
local targetNumber = math.random(1,2)
local targetPlate = parent[targetNumber]
targetPlate.CanCollide = false

local function Broken(hit)
	local player = players:GetPlayerFromCharacter(hit.Parent)
	if player then
		targetPlate.Anchored = false
	end
end

targetPlate.Touched:Connect(Broken)