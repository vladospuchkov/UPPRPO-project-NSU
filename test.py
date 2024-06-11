import pytest
from PyQt5.QtWidgets import QApplication, QPushButton
from PyQt5.QtTest import QTest
from PyQt5.QtCore import Qt

from main import AppWindow  

@pytest.fixture
def app(qtbot):
    test_app = AppWindow()
    qtbot.addWidget(test_app)
    return test_app

# CalculatorWindow Tests
def test_calculator_addition(app, qtbot):
    app.stacked_widget.setCurrentIndex(0)  # переключаемся на окно калькулятора

    calculator = app.calculator_window
    qtbot.mouseClick(calculator.findChild(QPushButton, '7'), Qt.LeftButton)
    qtbot.mouseClick(calculator.findChild(QPushButton, '+'), Qt.LeftButton)
    qtbot.mouseClick(calculator.findChild(QPushButton, '8'), Qt.LeftButton)
    qtbot.mouseClick(calculator.findChild(QPushButton, '='), Qt.LeftButton)

    assert calculator.result_display.text() == '15'

def test_calculator_subtraction(app, qtbot):
    app.stacked_widget.setCurrentIndex(0)

    calculator = app.calculator_window
    qtbot.mouseClick(calculator.findChild(QPushButton, '9'), Qt.LeftButton)
    qtbot.mouseClick(calculator.findChild(QPushButton, '-'), Qt.LeftButton)
    qtbot.mouseClick(calculator.findChild(QPushButton, '4'), Qt.LeftButton)
    qtbot.mouseClick(calculator.findChild(QPushButton, '='), Qt.LeftButton)

    assert calculator.result_display.text() == '5'

def test_calculator_multiplication(app, qtbot):
    app.stacked_widget.setCurrentIndex(0)

    calculator = app.calculator_window
    qtbot.mouseClick(calculator.findChild(QPushButton, '3'), Qt.LeftButton)
    qtbot.mouseClick(calculator.findChild(QPushButton, '*'), Qt.LeftButton)
    qtbot.mouseClick(calculator.findChild(QPushButton, '4'), Qt.LeftButton)
    qtbot.mouseClick(calculator.findChild(QPushButton, '='), Qt.LeftButton)

    assert calculator.result_display.text() == '12'

def test_calculator_division(app, qtbot):
    app.stacked_widget.setCurrentIndex(0)

    calculator = app.calculator_window
    qtbot.mouseClick(calculator.findChild(QPushButton, '8'), Qt.LeftButton)
    qtbot.mouseClick(calculator.findChild(QPushButton, '/'), Qt.LeftButton)
    qtbot.mouseClick(calculator.findChild(QPushButton, '2'), Qt.LeftButton)
    qtbot.mouseClick(calculator.findChild(QPushButton, '='), Qt.LeftButton)

    assert calculator.result_display.text() == '4'

# TimerWindow Tests
def test_timer_start_stop(app, qtbot):
    app.stacked_widget.setCurrentIndex(1)

    timer = app.timer_window
    qtbot.mouseClick(timer.start_button, Qt.LeftButton)
    QTest.qWait(100)
    qtbot.mouseClick(timer.stop_button, Qt.LeftButton)

    elapsed_time = timer.timer_lcd.value()
    assert elapsed_time > 0

def test_timer_reset(app, qtbot):
    app.stacked_widget.setCurrentIndex(1)

    timer = app.timer_window
    qtbot.mouseClick(timer.start_button, Qt.LeftButton)
    QTest.qWait(100)
    qtbot.mouseClick(timer.stop_button, Qt.LeftButton)
    qtbot.mouseClick(timer.reset_button, Qt.LeftButton)

    assert timer.timer_lcd.value() == 0

# NotesWindow Tests
def test_notes_save_load(app, qtbot):
    app.stacked_widget.setCurrentIndex(2)

    notes = app.notes_window
    notes.notes_edit.setText("Test note")
    qtbot.mouseClick(notes.save_button, Qt.LeftButton)

    notes.notes_edit.clear()
    qtbot.mouseClick(notes.load_button, Qt.LeftButton)

    assert notes.notes_edit.toPlainText() == "Test note"

def test_notes_multiple(app, qtbot):
    app.stacked_widget.setCurrentIndex(2)

    notes = app.notes_window
    notes.notes_edit.setText("First note")
    qtbot.mouseClick(notes.save_button, Qt.LeftButton)

    notes.notes_edit.setText("Second note")
    qtbot.mouseClick(notes.save_button, Qt.LeftButton)

    notes.notes_edit.clear()
    qtbot.mouseClick(notes.load_button, Qt.LeftButton)

    assert notes.notes_edit.toPlainText() == "First note\nSecond note"

# ClickerWindow Tests
def test_clicker(app, qtbot):
    app.stacked_widget.setCurrentIndex(3)

    clicker = app.clicker_window
    qtbot.mouseClick(clicker.click_button, Qt.LeftButton)
    qtbot.mouseClick(clicker.click_button, Qt.LeftButton)

    assert clicker.click_count == 2
    assert "Clicks: 2" in clicker.click_display.text()

def test_clicker_reset(app, qtbot):
    app.stacked_widget.setCurrentIndex(3)

    clicker = app.clicker_window
    qtbot.mouseClick(clicker.click_button, Qt.LeftButton)
    qtbot.mouseClick(clicker.click_button, Qt.LeftButton)
    qtbot.mouseClick(clicker.reset_button, Qt.LeftButton)

    assert clicker.click_count == 0
    assert "Clicks: 0" in clicker.click_display.text()

# RandomizerWindow Tests
def test_randomizer(app, qtbot):
    app.stacked_widget.setCurrentIndex(4)

    randomizer = app.randomizer_window
    randomizer.min_input.setValue(1)
    randomizer.max_input.setValue(100)
    qtbot.mouseClick(randomizer.generate_button, Qt.LeftButton)

    result_text = randomizer.result_display.text()
    assert "Result:" in result_text
    random_value = int(result_text.split(':')[-1].strip())
    assert 1 <= random_value <= 100

def test_randomizer_min_max(app, qtbot):
    app.stacked_widget.setCurrentIndex(4)

    randomizer = app.randomizer_window
    randomizer.min_input.setValue(50)
    randomizer.max_input.setValue(60)
    qtbot.mouseClick(randomizer.generate_button, Qt.LeftButton)

    result_text = randomizer.result_display.text()
    assert "Result:" in result_text
    random_value = int(result_text.split(':')[-1].strip())
    assert 50 <= random_value <= 60

if __name__ == "__main__":
    pytest.main()
