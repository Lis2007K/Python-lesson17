import streamlit as st
from abc import ABC, abstractmethod


class Person(ABC):
    """
    Abstract base class representing a person.
    """

    def __init__(self, name, age, weight, height):
        self.name = name
        self.age = age
        self._weight = weight
        self._height = height

    @property
    def weight(self):
        return self._weight

    @weight.setter
    def weight(self, value):
        if value < 0:
            raise ValueError("Weight cannot be negative")
        self._weight = value

    @property
    def height(self):
        return self._height

    @height.setter
    def height(self, value):
        if value < 0:
            raise ValueError("Height cannot be negative")
        self._height = value

    @abstractmethod
    def calculate_bmi(self):
        pass


class RegularPerson(Person):
    """
    Concrete implementation of Person.
    """

    def calculate_bmi(self):
        if self.height == 0:
            return 0
        return self.weight / ((self.height / 100) ** 2)  # height in cm to m


# --- Streamlit App ---
st.set_page_config(page_title="BMI Calculator", page_icon="💪", layout="centered")

st.title(" BMI Calculator")
st.markdown("### Enter your personal details")

name = st.text_input("Name")
age = st.number_input("Age", min_value=0, max_value=120, step=1)
weight = st.number_input("Weight (kg)", min_value=0.0, step=0.1)
height = st.number_input("Height (cm)", min_value=0.0, step=0.1)

if st.button("Calculate BMI"):
    try:
        person = RegularPerson(name, age, weight, height)
        bmi = person.calculate_bmi()

        st.success(f"**{name}**, your BMI is: **{bmi:.2f}**")

        if bmi < 18.5:
            st.info("You are underweight.")
        elif 18.5 <= bmi < 24.9:
            st.success("You have a normal weight.")
        elif 25 <= bmi < 29.9:
            st.warning("You are overweight.")
        else:
            st.error("You are obese.")

    except ValueError as e:
        st.error(str(e))
