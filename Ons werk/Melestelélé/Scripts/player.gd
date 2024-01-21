extends CharacterBody2D

@export var SPEED = 600
@export var GRAVITY = 100
@export var JUMP = 1200
@export var JUMP_VELOCITY = -1200
@export var DASH_LENGHT = 12000
@onready var deathAnimation = get_parent().get_node("AnimationPlayer")
var canDash = true
var canDoubleJump = true
var canJump
var screen_size = null
var player = null


func _ready():
	screen_size = get_viewport_rect().size
	player = $AnimatedSprite2D

func _physics_process(delta):
	
	
	if position.y > 1000:
		deathAnimation.play("fade_in")
	
	movement()

func movement():
	velocity.y += GRAVITY
	if is_on_floor():
		if player.animation == "fall":
			canDash = true			
			player.stop()
		velocity.y = 0
		canJump = true		
		canDoubleJump = true

		if Input.is_action_just_pressed("jump"):
			velocity.y -= JUMP
			canJump = false

	else:
		if Input.is_action_just_pressed("jump") and canDoubleJump == true:
			if canJump == true:
				velocity.y = JUMP_VELOCITY	
				canJump = false		
			else:	
				velocity.y = JUMP_VELOCITY
				canDoubleJump = false
		
		if velocity.y < 0:
			player.play("jump")

		else:
			player.play("fall")

	if Input.is_action_pressed("move_right"):
		player.flip_h = false
		velocity.x = +SPEED

		if player.animation == "idle" or !player.is_playing():
			player.play("run")


	elif Input.is_action_pressed("move_left"):
		player.flip_h = true
		velocity.x = -SPEED

		if player.animation == "idle" or !player.is_playing():
			player.play("run")

	else:
		velocity.x = 0

		if velocity.x == 0 and velocity.y == 0:
			player.play("idle")
	
	
	if Input.is_action_just_pressed("dash"):
		if canDash == true:
			if player.flip_h == true:
				velocity.x -= DASH_LENGHT

			else:
				velocity.x += DASH_LENGHT
				
			canDash = false

	move_and_slide()


func _on_animation_player_animation_finished(anim_name):
	if anim_name == "fade_in":
		position = Vector2(50, 447)
		deathAnimation.play("fade_out")


func _on_collision_shape_2d_child_entered_tree(node):
	print(node)
