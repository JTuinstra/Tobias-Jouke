extends Area2D

@export var level_2 : PackedScene

func _on_body_entered(body):
	get_tree().change_scene_to_packed(level_2)
