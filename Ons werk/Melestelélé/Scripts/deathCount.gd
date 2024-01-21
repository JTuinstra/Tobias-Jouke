extends Label
var deathCount = 0
# Called when the node enters the scene tree for the first time.
func _ready():
	pass # Replace with function body.
	text = str(deathCount)
	


func _on_animation_player_animation_finished(anim_name):
	if anim_name == "fade_in":
		deathCount += 1
		text = str(deathCount)
