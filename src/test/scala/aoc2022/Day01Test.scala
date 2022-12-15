package aoc2022

import org.scalatest.funsuite.AnyFunSuite

class Day01Test extends AnyFunSuite {

  val sample = io.Source.fromResource("aoc2022/Day01test.in").mkString

  test("Part 1 should handle sample input correctly") {
    assert(Day01.part1(sample) == 24000)
  }

  test("Part 2 should handle sample input correctly") {
    assert(Day01.part2(sample) == 45000)
  }
}
