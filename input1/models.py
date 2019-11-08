from django.db import models
from input1.choices import *

# Create your models here.

class Student(models.Model):
	name = models.CharField(max_length=256)
	reg_no = models.PositiveIntegerField()

	def __str__(self):
		return self.name

class Division(models.Model):

	name = models.CharField(max_length=3,choices=division_choices)
	def __str__(self):
		return self.name

class Faculty(models.Model):
	name = models.CharField(max_length=256)
	id_no = models.PositiveIntegerField()
	division= models.ForeignKey(Division,on_delete=models.CASCADE)
	designation=models.CharField(max_length=256,null=True)

	def __str__(self):
		return self.name

class School(models.Model):
	name = models.CharField(max_length=3,choices=school_choices)
	division=models.ForeignKey(Division,on_delete=models.CASCADE)
	def __str__(self):
		return self.name

class Department(models.Model):
	name = models.CharField(max_length=3,choices=department_choices)
	school=models.ForeignKey(School,on_delete=models.CASCADE)

	def __str__(self):
		return self.name

class Branch(models.Model):
	name = models.CharField(max_length=3,choices=branch_choices)
	department=models.ForeignKey(Department,on_delete=models.CASCADE)

	def __str__(self):
		return self.name



class Course(models.Model):
	division = models.ForeignKey(Division,on_delete=models.CASCADE)
	school = models.ForeignKey(School,on_delete=models.CASCADE)
	department = models.ForeignKey(Department,on_delete=models.CASCADE)
	branch = models.ForeignKey(Branch,on_delete=models.CASCADE)
	course_code = models.CharField(max_length=3,choices=course_choices)
		
	def __str__(self):
		return self.course_code

class Room(models.Model):
 	room_no = models.PositiveIntegerField()
 	block = models.PositiveIntegerField(choices=block_choices)

 	def __str__(self):
 		return self.room_no
 		
class Booking(models.Model):
	
	division = models.CharField(max_length=3,choices=division_choices,null=True)
	school = models.ForeignKey(School,on_delete=models.CASCADE,null=True)
	department = models.ForeignKey(Department,on_delete=models.CASCADE,null=True)
	branch = models.ForeignKey(Branch,on_delete=models.CASCADE,null=True)
	course_code = models.ForeignKey(Course, on_delete=models.CASCADE,null=True)
	date = models.DateField(max_length=256)
	semester = models.PositiveIntegerField(choices=semester_choices)
	time = models.TimeField(max_length=256)
	room_no = models.PositiveIntegerField()
	block = models.PositiveIntegerField(choices=block_choices)
	faculty_assigned=models.ForeignKey(Faculty, on_delete=models.CASCADE)
		
	def __str__(self):
		return self.primary_key

