{
 "cells": [
  {
   "cell_type": "markdown",
   "id": "d3d28987",
   "metadata": {},
   "source": [
    "### User Information Collection \n",
    "This notebook collects a user’s name, age, and favorite color, displaying them back to the user. This helps practice basic Python syntax, input/output, and string formatting.\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "id": "ed693f45",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "What is your name: A\n",
      "How old are you: 2\n",
      "What is your favorite color: red\n"
     ]
    }
   ],
   "source": [
    "#collecting your information\n",
    "\n",
    "name  = input(\"What is your name: \")\n",
    "age   = input(\"How old are you: \")\n",
    "color = input(\"What is your favorite color: \")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 7,
   "id": "dbe0def0",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "User information \n",
      "name: A\n",
      "age: 2\n",
      "color: red\n"
     ]
    }
   ],
   "source": [
    "print(\"User information \")\n",
    "print(\"name: \" + name)\n",
    "print(\"age: \" +  age)\n",
    "print(\"color: \" + color)"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "c3964d2d",
   "metadata": {},
   "source": [
    "### Explanation\n",
    "- `input()` function is used to capture user input as a string.\n",
    "- `print()` function is used to display output on the console.\n"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.9.13"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
