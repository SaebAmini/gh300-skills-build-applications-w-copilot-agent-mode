from django.core.management.base import BaseCommand
from octofit_tracker.models import User, Team, Activity, Leaderboard, Workout
from datetime import datetime, timedelta
import random


class Command(BaseCommand):
    help = 'Populate the octofit_db database with test data'

    def handle(self, *args, **options):
        self.stdout.write(self.style.SUCCESS('Clearing existing data...'))
        
        # Delete existing data
        User.objects.all().delete()
        Team.objects.all().delete()
        Activity.objects.all().delete()
        Leaderboard.objects.all().delete()
        Workout.objects.all().delete()

        self.stdout.write(self.style.SUCCESS('Creating teams...'))
        
        # Create teams
        team_marvel = Team.objects.create(
            name='Team Marvel',
            captain_id='1',
            member_count=5
        )
        
        team_dc = Team.objects.create(
            name='Team DC',
            captain_id='6',
            member_count=5
        )

        self.stdout.write(self.style.SUCCESS('Creating users...'))
        
        # Create users for Team Marvel
        marvel_users = [
            {'name': 'Iron Man', 'email': 'ironman@marvel.com', 'age': 48, 'fitness_level': 'Advanced'},
            {'name': 'Captain America', 'email': 'cap@marvel.com', 'age': 100, 'fitness_level': 'Elite'},
            {'name': 'Thor', 'email': 'thor@marvel.com', 'age': 1500, 'fitness_level': 'Elite'},
            {'name': 'Black Widow', 'email': 'blackwidow@marvel.com', 'age': 35, 'fitness_level': 'Advanced'},
            {'name': 'Hulk', 'email': 'hulk@marvel.com', 'age': 45, 'fitness_level': 'Elite'},
        ]
        
        # Create users for Team DC
        dc_users = [
            {'name': 'Batman', 'email': 'batman@dc.com', 'age': 42, 'fitness_level': 'Advanced'},
            {'name': 'Superman', 'email': 'superman@dc.com', 'age': 35, 'fitness_level': 'Elite'},
            {'name': 'Wonder Woman', 'email': 'wonderwoman@dc.com', 'age': 3000, 'fitness_level': 'Elite'},
            {'name': 'Flash', 'email': 'flash@dc.com', 'age': 28, 'fitness_level': 'Advanced'},
            {'name': 'Aquaman', 'email': 'aquaman@dc.com', 'age': 38, 'fitness_level': 'Advanced'},
        ]
        
        created_users = []
        user_id = 1
        
        for user_data in marvel_users:
            user = User.objects.create(
                email=user_data['email'],
                name=user_data['name'],
                age=user_data['age'],
                fitness_level=user_data['fitness_level'],
                team_id=str(team_marvel.id)
            )
            created_users.append((user_id, user))
            user_id += 1
        
        for user_data in dc_users:
            user = User.objects.create(
                email=user_data['email'],
                name=user_data['name'],
                age=user_data['age'],
                fitness_level=user_data['fitness_level'],
                team_id=str(team_dc.id)
            )
            created_users.append((user_id, user))
            user_id += 1

        self.stdout.write(self.style.SUCCESS('Creating activities...'))
        
        # Create activities for each user
        activity_types = ['Running', 'Cycling', 'Swimming', 'Weight Training', 'Yoga']
        
        for uid, user in created_users:
            for _ in range(random.randint(3, 7)):
                activity_type = random.choice(activity_types)
                duration = random.randint(20, 90)
                distance = round(random.uniform(1, 15), 2) if activity_type in ['Running', 'Cycling', 'Swimming'] else None
                calories = duration * random.randint(5, 12)
                
                Activity.objects.create(
                    user_id=str(uid),
                    type=activity_type,
                    duration=duration,
                    distance=distance,
                    calories=calories
                )

        self.stdout.write(self.style.SUCCESS('Creating leaderboard entries...'))
        
        # Create leaderboard based on activities
        rank = 1
        for uid, user in sorted(created_users, key=lambda x: random.randint(100, 1000), reverse=True):
            total_points = Activity.objects.filter(user_id=str(uid)).count() * random.randint(50, 150)
            
            Leaderboard.objects.create(
                user_id=str(uid),
                user_name=user.name,
                team_id=user.team_id,
                team_name='Team Marvel' if user.team_id == str(team_marvel.id) else 'Team DC',
                total_points=total_points,
                rank=rank
            )
            rank += 1

        self.stdout.write(self.style.SUCCESS('Creating workouts...'))
        
        # Create workout suggestions
        workouts = [
            {
                'name': 'Super Soldier Strength Training',
                'description': 'High-intensity strength training inspired by Captain America',
                'difficulty': 'Advanced',
                'duration': 45,
                'type': 'Weight Training',
                'calories_estimate': 400
            },
            {
                'name': 'Speed Force Cardio',
                'description': 'Lightning-fast cardio workout for maximum endurance',
                'difficulty': 'Elite',
                'duration': 30,
                'type': 'Running',
                'calories_estimate': 350
            },
            {
                'name': 'Amazonian Warrior Yoga',
                'description': 'Flexibility and strength yoga routine',
                'difficulty': 'Intermediate',
                'duration': 60,
                'type': 'Yoga',
                'calories_estimate': 200
            },
            {
                'name': 'Dark Knight Circuit',
                'description': 'Batman-inspired full-body circuit training',
                'difficulty': 'Advanced',
                'duration': 40,
                'type': 'Weight Training',
                'calories_estimate': 380
            },
            {
                'name': 'Asgardian Power Lift',
                'description': 'Heavy lifting routine worthy of Thor',
                'difficulty': 'Elite',
                'duration': 50,
                'type': 'Weight Training',
                'calories_estimate': 450
            },
            {
                'name': 'Atlantean Swim Session',
                'description': 'Aquaman-approved swimming workout',
                'difficulty': 'Intermediate',
                'duration': 45,
                'type': 'Swimming',
                'calories_estimate': 320
            },
        ]
        
        for workout_data in workouts:
            Workout.objects.create(**workout_data)

        self.stdout.write(self.style.SUCCESS('Database populated successfully!'))
        self.stdout.write(self.style.SUCCESS(f'Created {User.objects.count()} users'))
        self.stdout.write(self.style.SUCCESS(f'Created {Team.objects.count()} teams'))
        self.stdout.write(self.style.SUCCESS(f'Created {Activity.objects.count()} activities'))
        self.stdout.write(self.style.SUCCESS(f'Created {Leaderboard.objects.count()} leaderboard entries'))
        self.stdout.write(self.style.SUCCESS(f'Created {Workout.objects.count()} workouts'))
