{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "66963baa",
   "metadata": {},
   "outputs": [],
   "source": [
    "from flask import Flask\n",
    "app = Flask(__name__)\n",
    "\n",
    "@app.route('/')\n",
    "def hello_world():\n",
    "    return 'Hello, World!'"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "16d87c56",
   "metadata": {},
   "outputs": [],
   "source": []
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
   "version": "3.9.6"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
