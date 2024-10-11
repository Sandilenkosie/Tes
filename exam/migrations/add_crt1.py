from django.db import migrations, transaction

def add_crt1(apps, schema_editor):
    Exam = apps.get_model('exam', 'Exam')
    Question = apps.get_model('exam', 'Question')
    Answer = apps.get_model('exam', 'Answer')
    Group = apps.get_model('exam', 'Group')


    with transaction.atomic():
        group, created = Group.objects.get_or_create(
            name='CRM-Exams',
            defaults={'description': 'Group for CRM related exams'}
        )

        # Create an exam instance and associate it with the group
        exam = Exam.objects.create(title='#CRM-1 Exam')

        # If you want to add the exam to the group (assuming a many-to-many relation):
        group.exams.add(exam)

        # Define questions and answers
        questions_data = [
                {
                    'text': 'Which two report formats can be used as a source report to configure a reporting snapshot?',
                    'answers': [
                        ('Tabular format', False),
                        ('Summary format', True),
                        ('Joined format', False),
                        ('Matrix format', True),
                    ]
                },
                {
                    'text': 'Universal Containers has two types of applicants, hourly and salary. How can you ensure the correct record creation?',
                    'answers': [
                        ('Create a permission set containing the salary record type and assign it to the appropriate users.', True),
                        ('Remove "create" permission for the salary applicant object for everyone except the manager and VP.', False),
                        ('Update the org-wide default to private and create a sharing rule.', False),
                        ('Configure the hourly record type as the default.', False),
                    ]
                },
                {
                    'text': 'Cloud Kicks works on an annual subscription model. When a sales rep marks an opportunity as closed won, a new opportunity should automatically be created for the renewal. The contracts team works outside of Salesforce but also needs to be notified about closed deals in order to initiate the contract process with the customer. Which automation solution would meet these requirements?',
                    'answers': [
                        ('Approval Process', False),
                        ('Validation Rule', False),
                        ('Process Builder', True),
                        ('Workflow Rule', False)
                    ]
                },
                {
                    'text': 'The finance manager at Universal Containers wants to receive a new business notification email each time a new client is won. The sales manager wants to receive a task letting them know to onboard the new client unless it is a top-tier client. Which automation tool should an app builder use to best address all these requests?',
                    'answers': [
                        ('Record-triggered flow', True),
                        ('Screen flow', False),
                        ('Apex', False),
                        ('Approval process', False)
                    ]
                },
                {
                    'text': 'Ursa Major Solar wants to see the Type field from the parent object Galaxy listed on the child record Star. The app builder is receiving an error stating "Picklist values are only supported in certain functions". What formula should an app builder use to achieve the desired result?',
                    'answers': [
                        ('ISPICKVAL(Galaxy__r.Type__c)', False),
                        ('VALUE(Galaxy__r.Type__c)', False),
                        ('TEXT(Galaxy__r.Type__c)', True),
                        ('FIND(Galaxy__r.Type__c)', False)
                    ]
                },
                {
                    'text': 'The CRM Manager at Universal Containers has requested that a custom text field be converted to a picklist in order to promote better data hygiene. What needs to be considered before changing the field type? (Choose 2 answers)',
                    'answers': [
                        ('Existing list views that reference the field may be deleted.', False),
                        ('Field references will be removed in Visualforce pages', False),
                        ('All data should be backed up before converting a text field.', True),
                        ('Changing a field type will remove existing field history.', True)
                    ]
                },
                {
                    'text': 'DreamHouse Realty requires that field value changes for certain fields such as Asking_Price__c and Real_Estate_Agent__c on their House__c custom object show up prominently on Chatter. What Chatter feature should the app builder utilize?',
                    'answers': [
                        ('Thanks', False),
                        ('Publisher Actions', False),
                        ('Topics', False),
                        ('Feed Tracking', True)
                    ]
                },
                {
                    'text': 'Universal Containers uses a custom object called Reviews to capture information generated by interviewers during the candidate process. The Review records are visible to any user that has access to the related custom Candidate record. The VP of Human Resources wants the comment field on the Review to be private to anyone outside of the HR department. How should the app builder meet this requirement?',
                    'answers': [
                        ('Create a page layout with the field and use field-level security to hide the field from all other users.', True),
                        ('Create an Apex sharing rule to share the field with users that have "HR" in their role.', False),
                        ('Create a sharing rule to share the field with the VP of HR with Role and Subordinates.', False),
                        ('Create a page layout with the field for HR users and another page layout without the field for all other users.', False)
                    ]
                },
                {
                    'text': 'Duplicate management for Leads has been implemented at Universal Containers but it seems duplicate leads are still being created. The Org Wide Default (OWD) is set to "Private" for Leads. Which two actions help prevent duplicate Leads from being created?',
                    'answers': [
                        ('Change the lead Hatching Rule to Block on create.', True),
                        ('Change OWD for Leads to Public Read.', False),
                        ('Change the Lead Duplicate Rule details to Bypass Sharing Rules.', True),
                        ('Change the Lead Assignment Rule to check for duplicates.', False),
                    ]
                },
                        {
                    'text': 'Because of the small screen, they currently have to scroll down the page to view the information for an account based on criteria about the related contact. Which solution should an app builder use to fulfill this requirement?',
                    'answers': [
                        ('Set the filter type on the component visibility to display based on user permissions, using custom permission to define the dynamic criteria.', False),
                        ('Add a related record component to the page layout.', False),
                        ('Set the component visibility to display based on an advanced filter type, using the contact field(s) to define the dynamic criteria.', True),
                        ('Hide the component behind a tab on the page layout.', False)
                    ]
                },
                {
                    'text': 'DreamHouse Realty wants to import its property records from an external system into Salesforce. The app builder will use an external ID field to house the property ID from the external system. Which two details should the app builder know when using external ID fields? Choose 2 answers.',
                    'answers': [
                        ('An external ID field can be a number field.', True),
                        ('An external ID field can be a URL field.', False),
                        ('An external ID field can be a phone field.', False),
                        ('An external ID field can be a text field.', True)
                    ]
                },
                {
                    'text': 'The convert button on leads should NOT appear until the lead status picklist is set to qualified. What should an app builder suggest to meet these requirements?',
                    'answers': [
                        ('Picklist dependency, page layouts, record types.', False),
                        ('Custom button, validation rule, record types.', True),
                        ('Process builder field update, quick action, record type.', False),
                        ('Page layout, record types, process builder field update.', False)
                    ]
                },
                {
                    'text': 'A sales manager has noticed that reps continue to input contacts directly in their phone instead of adding them to Salesforce. What should an app builder recommend to ensure the data makes it into Salesforce?',
                    'answers': [
                        ('Enable in-app notifications every time a contact is created.', False),
                        ('Allow Salesforce to import Contacts from mobile device Contact lists.', True),
                        ('Enable offline create, edit, and delete in Salesforce for Android and iOS.', True),
                        ('Allow users to relate a contact to multiple accounts.', False)
                    ]
                },
                {
                    'text': 'Universal Containers would like to embed a chart of all related Opportunities, by stage, on the Account detail page. Which type of report should the App Builder create to add to the Account page layout?',
                    'answers': [
                        ('A summary report on the Opportunity object.', True),
                        ('A summary report on the Account object.', False),
                        ('A tabular report on the Account object.', False),
                        ('A tabular report on the Opportunity object.', False)
                    ]
                },
                {
                    'text': 'The app builder at Cloud Kicks has created a custom object named Delivery__c to track the details of products shipped to customers. Which two actions should the app builder take to prevent users in the shipping department from deleting delivery records?',
                    'answers': [
                        ('Remove the Delete permission from the Shipper profile.', True),
                        ('Change the organization-wide default of deliveries to Private.', False),
                        ('Remove the delete button from the Delivery page layout.', False),
                        ('Use a permission set to remove the Delete permission.', True)
                    ]
                },
                {
                    'text': 'Northern Trail Outfitters uses a custom object to track travel requests. Rangers want to have automatic posts on a record whenever a travel request has been approved. Which feature should be used to accomplish this?',
                    'answers': [
                        ('Auto-response rule.', False),
                        ('Workflow rule.', False),
                        ('Feed tracking.', True),
                        ('Feed quick action.', False)
                    ]
                },
                {
                    'text': 'Universal Containers has a custom picklist called Support Level on the Account object. They would like to show the real-time value of Support Level on all case records. How should an app builder implement this requirement?',
                    'answers': [
                        ('Create a formula field on the Case object using the TEXT function.', True),
                        ('Create a formula field on the Account object using the ISPICKVAL function.', False),
                        ('Create a Process Builder and use a field update on the Case object.', False),
                        ('Create a roll-up summary field using Support Level on the Account object.', False)
                    ]
                },

        {
                    'text': 'Universal Containers has a custom picklist called Support Level on the Account object. They would like to show the real-time value of Support Level on all case records. How should an app builder implement this requirement?',
                    'answers': [
                        ('Create a formula field on the Case object using the TEXT function.', True),
                        ('Create a formula field on the Account object using the ISPICKVAL function.', False),
                        ('Create a Process Builder and use a field update on the Case object.', False),
                        ('Create a roll-up summary field using Support Level on the Account object.', False)
                    ]
                },
                {
                    'text': 'Universal Container wants customers to be able to open cases from a public-facing website. What should the app builder use to enable visitors to the website?',
                    'answers': [
                        ('Outbound message', False),
                        ('Web-to-case', True),
                        ('Screen flow', False),
                        ('Email-to-case', False)
                    ]
                },
                {
                    'text': 'Universal Containers (UC) has several picklist fields on the Account object whose values are routinely modified to meet changing business requirements. Due to these revolving changes, UC has a high number of inactive picklist values that are impacting system performance and user experience. What can the app builder do to alleviate this issue?',
                    'answers': [
                        ('Establish upper bound on existing picklists in Picklist Settings.', False),
                        ('Set up Global Values in Picklist Value Sets.', True),
                        ('Remove upper bound on inactive picklist values in Picklist Settings.', False),
                        ('Convert the picklist fields to a different field type that will still meet the business requirements.', False)
                    ]
                },
                {
                    'text': 'What is the process to upgrade an unmanaged package that is currently installed in production?',
                    'answers': [
                        ('Uninstall the current version and install the new version.', False),
                        ('Use the Install Wizard to install the upgrade to production.', False),
                        ('Install the new version to a Developer org then deploy to production.', False),
                        ('Click the update link on the Installed Packages page.', True)
                    ]
                },
                {
                    'text': 'Cloud Kicks\'s management team frequently travels and wants to approve requests from their team on the go via Chatter. Where would an app builder enable this ability?',
                    'answers': [
                        ('Chatter Feed Tracking.', False),
                        ('Object Settings.', False),
                        ('Chatter Settings.', True),
                        ('Approval Process Settings.', False)
                    ]
                },
                {
                    'text': 'Universal Containers has a custom picklist called Support Level on the Account object. They would like to show the real-time value of Support Level on all case records. How should an app builder implement this requirement?',
                    'answers': [
                        ('Create a formula field on the Case object using the TEXT function.', True),
                        ('Create a formula field on the Account object using the ISPICKVAL function.', False),
                        ('Create a Process Builder and use a field update on the Case object.', False),
                        ('Create a roll-up summary field using Support Level on the Account object.', False)
                    ]
                },
                        {
                    'text': "Universal Containers implemented an application process that uses custom objects Internships and Applications. "
                            "The organization-wide default for Internships has been set to private and is the master in the master-detail "
                            "relationship with Applications. How should an app builder configure the proper access?",
                    'answers': [
                        ('Set the organization-wide default on the Applications object to Read/Write.', False),
                        ('Add a sharing rule that grants the users Read/Write access to the Internship records.', False),
                        ('Create a queue for the web applications and assign access to the users who will be editing the records.', False),
                        ('Create a sharing rule that grants the users Read/Write access to the Application records.', True)
                    ]
                },
                {
                    'text': "An app builder needs to create new automation on an object. What best practice should the app builder follow "
                            "when building out automation?",
                    'answers': [
                        ('One Workflow rule per object.', False),
                        ('One Flow per object.', False),
                        ('One invocable process per object.', False),
                        ('One record change process per object.', True)
                    ]
                },
                        {
                    'text': 'The sales Operations team at AWS Computing deletes accounts for a variety of reasons. The sales ops director is worried that the Sales team may delete accounts that sales reps are actively selling into. How should the app builder keep accounts with open opportunities from being deleted?',
                    'answers': [
                        ('Create an Apex Trigger on the Account object', False),
                        ('Create a validation rule on the Account object', True),
                        ('Remove the delete button on the account layout', False),
                        ('Remove the Delete permission from the Sales Rep profile', False)
                    ]
                },
                {
                    'text': 'Universal Containers would like to collaborate with its customers within Salesforce, and has decided to enable the "Allow Customer Invitations" Chatter setting. What permission is granted to Customers when invited to Chatter Group?',
                    'answers': [
                        ('The ability to invite members to groups of which they are a member', False),
                        ('The ability to @mention accounts of which they are a contact.', False),
                        ('The ability to request access to public groups', False),
                        ('The ability to interact with members of their groups', True)
                    ]
                },
                {
                    'text': 'A business user wants a quick way to edit a record\'s status and enter a custom due date field from the record\'s feed in Salesforce Mobile App. What should be used to accomplish this?',
                    'answers': [
                        ('Custom action', True),
                        ('Custom button', False),
                        ('Custom quick access link', False),
                        ('Custom URL formula Field', False)
                    ]
                },
                {
                    'text': 'Ursa Major Solar\'s sales team has been struggling to enter data on mobile since rollout; the team dislikes scrolling through all of the fields to input only the necessary data. How could the app builder solve this with minimal impact to desktop users?',
                    'answers': [
                        ('Filter components by device using Form Factor.', True),
                        ('Reorder the fields to make sense for the reps when in the field.', False),
                        ('Update the training documentation with better screenshots.', False),
                        ('Deselect the phone radio button on the Lightning record page assignment.', False)
                    ]
                },
                {
                    'text': 'Universal Containers is setting up Salesforce for the first time. Management wants the sales and marketing teams to have different navigation names in the Salesforce1 mobile app. Which option is available to an app builder to satisfy the requirement?',
                    'answers': [
                        ('Create sales and marketing profiles to ensure read access to different objects', False),
                        ('Create roles for sales and marketing and assign a custom homepage layout for each role.', False),
                        ('Create mobile navigation menus for both the sales and marketing profiles.', True),
                        ('Create public groups for sales and marketing and create mobile navigation menus for each group.', False)
                    ]
                },
                {
                    'text': 'Northern Trail Outfitters (NTO) has created the custom objects Trail and Park in Salesforce to track trails and parks respectively. NTO wants to track the total number of trails a park has on the park record without writing any code. Which two actions should an app builder take to accomplish this requirement?',
                    'answers': [
                        ('Use a formula field on the Park record to show the total number of trails.', False),
                        ('Use a roll-up summary field on the Park record to show the total number of Trails.', True),
                        ('Use a master-detail relationship between the Park and Trail objects.', True),
                        ('Use a lookup relationship between the Park and Trail objects.', False)
                    ]
                },
                {
                    'text': 'DreamHouse Realty wants to track how many lifts are being installed into customer garages. The To Be Installed custom checkbox field on the custom Lift object should be checked and an external system should be notified via an outbound message the next day when a lift is sold. What automation tool should be used to complete this task?',
                    'answers': [
                        ('Approval process', False),
                        ('Workflow', False),
                        ('Flow', False),
                        ('Process Builder', True)
                    ]
                },
                {
                    'text': 'Cloud Kicks (CK) tracks the support level of its customers on the account record page. CK wants to show a text notification on a case record page when the related account is a platinum-level customer. How could an app builder meet this requirement?',
                    'answers': [
                        ('Add a rich text area to the Case Lightning page > Set the component visibility of the rich text area to show when the account support level is platinum.', False),
                        ('Create a text-only Visualforce page > Drag the Visualforce component into the Case page layout > Set its visibility to show when the account support level is platinum.', True),
                        ('Create a text-only Visualforce page > Clone the case page layout > Drag the Visualforce component into the page, and assign the layout to platinum cases.', False),
                        ('Clone the Case Lightning page > Add a rich text area to the new page, and assign this page to platinum accounts.', False)
                    ]
                },
            ]


        for question_data in questions_data:
                # Automatically set multiple_correct if more than one answer is correct
                multiple_correct = sum(1 for answer in question_data['answers'] if answer[1]) > 1
                question = Question.objects.create(
                    exam=exam,
                    text=question_data['text'],
                    multiple_correct=multiple_correct
                )
                for answer_text, is_correct in question_data['answers']:
                    Answer.objects.create(question=question, text=answer_text, is_correct=is_correct)

class Migration(migrations.Migration):

    dependencies = [
        # Add your app's dependencies here
        ('exam', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(add_crt1, atomic=False),
    ]
