;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;
; CapsLock + hjkl 鼠标上下左右移动
; TODO 加速移动
;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;
CapsLock & h::
CapsLock & l::
CapsLock & j::
CapsLock & k::
mouse_move()
return

mouse_move(){
	Horizontal := 0
	vertical := 0
	if GetKeystate("h","P") {
		Horizontal := Horizontal - 1
	}
	if GetKeystate("l","P") {
		Horizontal := Horizontal + 1
	}
	if GetKeystate("j","P") {
		vertical := vertical - 1
	}
	if GetKeystate("k","P") {
		vertical := vertical + 1
	}
	speed := 10
	Horizontal := Horizontal * speed
	vertical := vertical * speed
	MouseMove, Horizontal, vertical, 0, R
}
