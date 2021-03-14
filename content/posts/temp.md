When insert:
1. operator select file in cms
2. cms server creat random fileId, use that id as file name in VOS
3. cms server uppload the file to VOS. (we need to add encryption here)
4. cms server upsert the BulkImportSourceModel data(need dataurl(with fileName.zip), importDataType, status is NOT_INSERTED)
5. Batch server go through all the the BulkImportSourceModel data
6. If there is banner file data that is  NOT_INSERTED, started process one by one
7. Create one collection with each fileId, insert all user data.
8. After one done, then update banner info collection with new fileId.

When search:
1. Get all active banner info at first, since we won't have much banners;
2. Check whether there is user mid limitation
3. If there is, get the fileId in banner info
4. User the fileId to confirm whether current user is target.