export const extractMessageMetadata = (tags) => {
    // Extract metadata from tags
    return {
      isChatMessage: tags.includes('type:chatmessage'),
      isUserStatus: tags.includes('type:userstatus'),
      from: tags.find(tag => tag.startsWith('from:')).split(':')[1],
      status: tags.find(tag => tag.startsWith('status:'))?.split(':')[1] || ''
    };
  };
  