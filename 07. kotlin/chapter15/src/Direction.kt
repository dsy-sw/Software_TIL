enum class Direction(val str: String) {
    NORTH("λΆ"),
    EAST("λ"),
    SOUTH("λ¨"),
    WEST("μ");

    override fun toString() = str
}

fun main() {
    var dir = Direction.EAST
    println(dir.str)

}