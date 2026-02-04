#!/usr/bin/env python3

from datetime import datetime
import argparse
import json

def checkDate(date):
    try:
        datetime.strptime(date, '%Y%m%d%H%M%S')
    except ValueError:
        raise SystemExit("\033[31mInvalid date format: YYYYMMDDHHMMSS\033[0m")

def checkUsers(date):
    allUsers = {}
    try:
        with open(f'{date}_users.json', 'r') as f:
            data = json.load(f)['data']
        for user in data:
            try:
                foundName = user['Properties']['samaccountname']
                foundOBID = user['ObjectIdentifier']
                allUsers[foundName] = foundOBID
            except:
                pass
        return allUsers
    except FileNotFoundError:
        print('Check Users Error: ...')

def checkGroups(date):
    allGroups = {}
    try:
        with open(f'{date}_groups.json', 'r') as f:
            data = json.load(f)['data']
    except FileNotFoundError:
        print('Check Groups Error: ...')
    for group in data:
        try:
            groupName = group['Properties']['samaccountname']
        except:
            pass
        one = group['Members']
        two = group['Aces']
        if not one:
            pass
        else:
            userIdentifiers = []
            groupPermissions = []
            for i in range(len(one)):
                if one[i]['ObjectType'] == 'User':
                    userIdentifier = f'{one[i]['ObjectIdentifier']}'
                    userIdentifiers.append(userIdentifier)
                else:
                    pass
            for i in range(len(two)):
                groupPermission = f'{two[i]['RightName']}'
                groupPermissions.append(groupPermission)
            both = [userIdentifiers, groupPermissions]
            #allGroups[str(groupName)] = userIdentifiers
            allGroups[str(groupName)] = both
    return allGroups

def main():
    ### * Settings * ###
    parser = argparse.ArgumentParser(description="...")
    parser.add_argument("--date", required=True, help="Example Timestamp: 2026129140449")
    parser.add_argument("--users", default=None, help="Example Users: all, 'J.BOLD@K2.THM', ---, ---")
    parser.add_argument("--groups", default=None, help="Example Groups: all, 'IT STAFF 1@K2.THM', ---, ---")
    args = parser.parse_args()
    ### * Date * ###
    date = args.date
    ### * User * ###
    users = args.users
    ### * Groups * ###
    groups = args.groups

    ### * Function Data* ###
    checkedDate = checkDate(date)
    funUsers = checkUsers(date)
    funGroups = checkGroups(date)
    
    ### * MAIN * ###
    if users == 'all':
        for q, w in zip(funUsers.keys(), funUsers.values()):
            print(f'\033[32mFound User: "{q}":"{w}"\033[0m')
        if groups == 'all':
            print('\033[31mGroup Error: Only use all with specific user.\033[0m')
        else:
            pass
    elif users in funUsers:
        groupList = list(funGroups.keys())
        userIDandPers = list(funGroups.values())
        if groups == 'all':
            usersID = funUsers[users]
            for groupName, userIDandPer in zip(groupList, userIDandPers):
                userID = userIDandPer[0]
                per = userIDandPer[1]
                if usersID in userID:
                    print(f'\033[32mGroup Name: {groupName}\033[0m')
                    for i in range(len(per)):
                        print(f'\t\033[32m{per[i]}\033[0m')
        elif groups in funGroups:
            print(f"Print Group Permissions!")
        else:
            print('\033[31mGroup Error: Only use USER:SPECIFIC with GROUP:ALL\033[0m')
    else:
        print('...')

if __name__ == "__main__":
    main()
