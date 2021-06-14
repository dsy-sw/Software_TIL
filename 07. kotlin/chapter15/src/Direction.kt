enum class Direction(val str: String) {
    NORTH("북"),
    EAST("동"),
    SOUTH("남"),
    WEST("서");

    override fun toString() = str
}

fun main() {
    var dir = Direction.EAST
    println(dir.str)

}