export default class MouseEvents {
	startMousePosition = {
		x: 0,
		y: 0
	}
	doubleTouch =  false
	touchDelay = 500
	doubleTouchTimeout = null
	isMouseDown = false
	isMousePositionUnchanged = false

	constructor(targetElement) {
		targetElement.addEventListener("mousedown", (e) => {
			this.handleMouseDown(e);
		}, false);

		targetElement.addEventListener("mouseup", (e) => {
			this.handleMouseUp(e);
		}, false);
	}

	handleMouseDown(e) {
		this.isMouseDown = true;

		this.startMousePosition = {
			x: e.clientX,
			y: e.clientY
		};

		if(this.doubleTouchTimeout == null) {
			this.doubleTouchTimeout = setTimeout(() => {
				if(!this.isMouseDown && this.isMousePositionUnchanged) {
					this.onClick();
				}
				this.doubleTouchTimeout = null;
			}, this.touchDelay);
		} else {
			if(this.doubleTouchTimeout != null) {
				clearTimeout(this.doubleTouchTimeout);
				this.doubleTouchTimeout = null;
				this.doubleTouch = true;
			}
		}

	}

	handleMouseUp(e) {
		this.isMouseDown = false;

		const currentMousePosition = {
			x: e.clientX,
			y: e.clientY
		};

		this.isMousePositionUnchanged = 
			currentMousePosition.x == this.startMousePosition.x && 
			currentMousePosition.y == this.startMousePosition.y;

		if(this.isMousePositionUnchanged) {
			if(this.doubleTouch) {
				this.onDoubleClick();
			}
		}

		if(this.doubleTouch) {
			this.doubleTouch = false;
		}
	}
}
