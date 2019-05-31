# Active Directory

## Summary

In Windows Active Directory, a group can consist of one or more users, as well as one or more groups.
For this problem, we want to search through our hierarchy of users and groups for a specific user

## Implementation

Similarly to problem #2 where we recursively searched for a file within directories, we are
searching through our group hierarchy for users. In our case, users are synonymous with files,
and directories are synonymous. Searching through all of the different users and subgroups
of our root group will take O(n), as we must traverse through every element in our data structure. The
space complexity is O(n), as we just need to continue storing each group or user as they are added. 